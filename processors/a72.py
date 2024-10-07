from m5.objects import *

# Pipeline taken from "Cortex®-A72 Software Optimization Guide" (March 10, 2015)
# Internal stuctures sizes from: https://chipsandcheese.com/2023/11/10/arms-cortex-a72-aarch64-for-the-masses/

# Integer ALU μops
class A72_Integer(FUDesc):
    opList = [OpDesc(opClass="IntAlu", opLat=1)]
    count = 2


# Integer shift-ALU, multiply, divide, CRC and sum-of-absolute-differences μops
class A72_MultiCycle(FUDesc):
    opList = [
        OpDesc(opClass="IntMult", opLat=3, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=12, pipelined=False),
        OpDesc(opClass="IprAccess", opLat=3, pipelined=True),
    ]
    count = 1


# ASIMD ALU, ASIMD misc, ASIMD integer multiply, FP convert, FP misc, FP add, FP multiply, FP divide, crypto μops
class A72_FP0(FUDesc):
    opList = [
        OpDesc(opClass="SimdAdd", opLat=3),
        OpDesc(opClass="SimdAlu", opLat=3),
        OpDesc(opClass="SimdCmp", opLat=3),
        OpDesc(opClass="SimdCvt", opLat=3),
        OpDesc(opClass="SimdMisc", opLat=3),
        OpDesc(opClass="SimdMult", opLat=4),
        OpDesc(opClass="SimdMultAcc", opLat=4),
        OpDesc(opClass="SimdSqrt", opLat=3),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatAlu", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatDiv", opLat=11, pipelined=False),
        OpDesc(opClass="SimdFloatMisc", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatMultAcc", opLat=4, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=9, pipelined=False),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="FloatMultAcc", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMisc", opLat=3, pipelined=True),
    ]
    count = 1


# ASIMD ALU, ASIMD misc, FP misc, FP add, FP multiply, FP sqrt, ASIMD shift μops
class A72_FP1(FUDesc):
    opList = [
        OpDesc(opClass="SimdAdd", opLat=3),
        OpDesc(opClass="SimdAddAcc", opLat=4),
        OpDesc(opClass="SimdCmp", opLat=3),
        OpDesc(opClass="SimdAlu", opLat=3),
        OpDesc(opClass="SimdMisc", opLat=3),
        OpDesc(opClass="SimdShift", opLat=3),
        OpDesc(opClass="SimdShiftAcc", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatAlu", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatMisc", opLat=3, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=20, pipelined=False),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="FloatMultAcc", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMisc", opLat=3, pipelined=True),
    ]
    count = 1


# Load/Store Units
class A72_Load(FUDesc):
    opList = [
        OpDesc(opClass="MemRead", opLat=4),
        OpDesc(opClass="FloatMemRead", opLat=4),
    ]
    count = 1


class A72_Store(FUDesc):
    opList = [
        OpDesc(opClass="MemWrite", opLat=1),
        OpDesc(opClass="FloatMemWrite", opLat=1),
    ]
    count = 1


# Functional Units for this CPU
class A72_FUPools(FUPool):
    FUList = [
        A72_Integer(),
        A72_MultiCycle(),
        A72_Load(),
        A72_Store(),
        A72_FP0(),
        A72_FP1(),
    ]


# Bi-Mode Branch Predictor
class A72_BP(BiModeBP):
    globalPredictorSize = 8192
    globalCtrBits = 2
    choicePredictorSize = 8192
    choiceCtrBits = 2

    btb = SimpleBTB(numEntries=2048, tagBits=18)
    ras = ReturnAddrStack(numEntries=16)

    instShiftAmt = 2


class A72_MMU(ArmMMU):
    itb = ArmTLB(entry_type="instruction", size=48)
    dtb = ArmTLB(entry_type="data", size=32)


width = 3
class A72_Core_Layout(DerivO3CPU):

    # Pipeline widths
    fetchWidth = 4
    fetchBufferSize = 16
    decodeWidth = width
    renameWidth = width
    dispatchWidth = width
    issueWidth = width
    wbWidth = width
    commitWidth = width
    squashWidth = width

    decodeToFetchDelay = 1
    renameToFetchDelay = 1
    iewToFetchDelay = 1
    commitToFetchDelay = 1
    renameToDecodeDelay = 1
    iewToDecodeDelay = 1
    commitToDecodeDelay = 1
    iewToRenameDelay = 1
    commitToIEWDelay = 1
    commitToRenameDelay = 1
    iewToCommitDelay = 1
    renameToROBDelay = 1
    forwardComSize = 5
    backComSize = 5

    LQEntries = 32
    SQEntries = 15
    LSQDepCheckShift = 0
    numPhysIntRegs = 64
    numPhysFloatRegs = 126
    numPhysVecRegs = 48
    numIQEntries = 32
    numROBEntries = 128

    trapLatency = 13

    fuPool = A72_FUPools()

    switched_out = False
    branchPred = A72_BP()
    mmu = A72_MMU()
