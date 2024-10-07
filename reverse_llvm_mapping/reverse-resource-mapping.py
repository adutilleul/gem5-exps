import argparse
import re

PATTERN_TD = re.compile(r"defm : (\w+)<(\w+),\s*\[([\w, _]+)\],\s*(\d+)")

PATTERN2_TD = re.compile(r"def : (\w+)<(\w+),\s*\[([\w, _]+)\]>;")

PATTERN_DEF_TD = (
    r"def : (\w+)<(\w+),\s*\[([\w, _]+)\]>\s*\{[^}]*let\s+Latency\s*=\s*(\d+);\n}"
)

COMBINED_DEF_TD = r"def\s+(\w+)\s*:\s*ProcResGroup<\[\s*([\w,\s]+)\s*\]>;"

RESOURCE_DEF_TD = r"def\s+(\w+)\s*:\s*ProcResource<(\d+)>;"

IS_PIPELINED: dict[str, bool] = dict({"FloatDiv": False, "FloatSqrt": False, "SimdFloatDiv": False, "SimdFloatSqrt": False, "IntDiv": False})

MANUAL_RESOURCES = dict(
    {
        "ADLPPort00_01_05_06_10": [
            "ADLPPort00",
            "ADLPPort01",
            "ADLPPort05",
            "ADLPPort06",
            "ADLPPort10",
        ],
        "ADLPPort04_09": ["ADLPPort04", "ADLPPort09"],
        "ADLPPort02_03_07_08_11": [
            "ADLPPort02",
            "ADLPPort03",
            "ADLPPort07",
            "ADLPPort08",
            "ADLPPort11",
        ],
    }
)


OP_TO_GEM5_OP = dict(
    {
        # Float
        "WriteFCmp": ["FloatCmp"],
        "WriteFAdd": ["FloatAdd"],
        "WriteFMul": ["FloatMult"],
        "WriteCvtSS2I": ["FloatCvt"],
        "WriteFDiv": ["FloatDiv"],
        "WriteFSqrt": ["FloatSqrt"],
        # SIMD Float
        "WriteFCmpX": ["SimdFloatCmp"],
        "WriteFAddX": ["SimdFloatAdd", "SimdFloatCmp"],  # MAXPS
        "WriteFMulX": ["SimdFloatMult"],
        "WriteCvtPS2I": ["SimdFloatCvt"],
        "WriteFDivX": ["SimdFloatDiv"],
        "WriteFSqrtX": ["SimdFloatSqrt"],
        # Int
        "WriteALU": ["IntAlu"],
        "WriteIMul32": ["IntMult"],
        "WriteDiv32": ["IntDiv"],
        # SIMD Int
        "WriteVecALUX": ["SimAdd"],
        "WriteVecLogicX": ["SimdAlu", "SimdCmp"],
        "WriteVecShiftX": ["SimdShift"],
        "WriteVecIMulX": ["SimdMult"],
        # Load/Store
        "WriteLoad": ["MemRead", "FloatMemRead"],
        "WriteStore": ["MemWrite", "FloatMemWrite"],
        # Misc
        "WriteBlend": ["SimdMisc"],
    }
)


class OpDescription:
    latency: int
    name: str

    def __init__(self, name: str, latency: int):
        self.name = name
        self.latency = latency

    def __str__(self):
        return f"""OpDesc(opClass="{self.name}", opLat={self.latency}, pipelined={IS_PIPELINED.get(self.name, True)})"""

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.latency == other.latency

    def __hash__(self):
        return hash((self.name, self.latency))


class PortDescription:
    name: str
    op_list: set[OpDescription]

    def __init__(self, name: str, op_list: set[OpDescription]):
        self.name = name
        self.op_list = op_list

    def __str__(self):
        return f"""class {self.name}(FUDesc):
    opList = [
        {",\n        ".join([str(op) for op in self.op_list])}
    ]
    count = 1"""

    def __repr__(self):
        return self.__str__()


def flatten_list(tl: list) -> list:
    return [item for sublist in tl for item in sublist]


def main():
    parser = argparse.ArgumentParser(description="Reverse resource mapping")
    parser.add_argument("filename", type=str, help="Filename for LLVM mapping")
    args = parser.parse_args()

    # get all lines from the file
    with open(args.filename, "r") as file:
        lines = file.readlines()

    with open(args.filename, "r") as file:
        text = file.read()

    uarch_ports: dict[str, PortDescription] = dict()
    ops_done: set[str] = set()
    combined_resources: dict[str, list[int]] = dict()

    # gather all resources
    match_defs = re.findall(RESOURCE_DEF_TD, text)
    for match_def in match_defs:
        name, lat = match_def
        uarch_ports[name] = PortDescription(name, set())

    # gather all combined resources
    match_defs = re.findall(COMBINED_DEF_TD, text)
    for match_def in match_defs:
        name, op_list = match_def
        combined_resources[name] = op_list.split(", ")

    # add manual resources
    for name, op_list in MANUAL_RESOURCES.items():
        combined_resources[name] = op_list

    def gather_port_oplist(op_list):
        ports = []
        for port in op_list.split(", "):
            if port in combined_resources:
                ports = ports + combined_resources[port]
            else:
                if len(port.split(",")) > 0:
                    for p in port.split(","):
                        if p in combined_resources:
                            ports = ports + combined_resources[p]
                        else:
                            ports.append(p)
                else:
                    ports.append(port)
        return ports

    for llvm_name, gem5_names in OP_TO_GEM5_OP.items():
        for line in lines:
            match = re.search(PATTERN_TD, line)
            match2 = re.search(PATTERN2_TD, line)
            if llvm_name in line and match:
                op_class = match.group(2)
                op_list = match.group(3)
                op_lat = match.group(4)

                if op_class == llvm_name and llvm_name not in ops_done:
                    ops_done.add(llvm_name)
                    ports = gather_port_oplist(op_list)
                    op_descs = [
                        OpDescription(gem5_name, int(op_lat))
                        for gem5_name in gem5_names
                    ]
                    for port in ports:
                        for op_desc in op_descs:
                            uarch_ports[port].op_list.add(op_desc)
            elif llvm_name in line and match2:
                op_class = match2.group(2)
                op_list = match2.group(3)
                op_lat = 1

                if op_class == llvm_name and llvm_name not in ops_done:
                    ops_done.add(llvm_name)
                    ports = gather_port_oplist(op_list)
                    op_descs = [
                        OpDescription(gem5_name, int(op_lat))
                        for gem5_name in gem5_names
                    ]
                    for port in ports:
                        for op_desc in op_descs:
                            uarch_ports[port].op_list.add(op_desc)
            elif llvm_name in line:
                match_defs = re.findall(PATTERN_DEF_TD, text)
                for match_def in match_defs:
                    name, op_class, op_list, op_lat = match_def
                    if op_class == llvm_name and llvm_name not in ops_done:
                        ops_done.add(llvm_name)
                        ports = gather_port_oplist(op_list)
                        op_descs = [
                            OpDescription(gem5_name, int(op_lat))
                            for gem5_name in gem5_names
                        ]
                        for port in ports:
                            for op_desc in op_descs:
                                uarch_ports[port].op_list.add(op_desc)

    # get ordered list of ports
    uarch_ports = dict(sorted(uarch_ports.items()))
    # filter out empty ports
    uarch_ports = {k: v for k, v in uarch_ports.items() if len(v.op_list) > 0}
    # remove divider ports from the list
    uarch_ports = {k: v for k, v in uarch_ports.items() if "Divider" not in k}
    for port in uarch_ports.values():
        print(port)
        print("\n")

    print("class ExecUnits(FUPool):")
    print("    FUList = [" + ", ".join([f"{port}()" for port in uarch_ports]) + "]")


if __name__ == "__main__":
    main()
