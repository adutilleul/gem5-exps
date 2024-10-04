## Requirements

 - gem5 24.04 (ghcr.io/gem5/ubuntu-24.04_all-dependencies:latest)

## Available configurations
 - SkyLake
 - Cortex-A72

## Running the simulation

If you have docker on your system, you can use the following command.

```sh
docker run --rm -u $UID:$GID -v `pwd`:`pwd` -w `pwd` ghcr.io/gem5/ubuntu-24.04_all-dependencies:latest run.py
```

The simulator will output the simulated time, the total instructions, and the total cycles.
For more detailed statistics, you will find `m5out/stats.txt` contains many detailed statistics.

By default, this runs a matrix multiple with ROI annotations and gives the number of cycles, instructions, and simulated time for only the ROI.

You don't need to modify anything to get started.
If you want to modify the workload implementation or modify the simulator, you can see below for details on how everything fits together.

### Options for the runscript

You can find details on the options you can pass to this simulation script by using `--help`.

```sh
docker run --rm -u $UID:$GID -v `pwd`:`pwd` -w `pwd` ghcr.io/gem5/ubuntu-24.04_all-dependencies:latest  run.py --help
```

### Choosing an output directory

When running the simulator and performing many experiments, you may want to use different directories for the output.
To do this, you can set the "outdir" on the command line.
Note that this is a *gem5* parameter, not a parameter to the script, so you need to set the parameter *before* `run.py` on the command line.
See below for an example.

```sh
docker run --rm -u $UID:$GID -v `pwd`:`pwd` -w `pwd` ghcr.io/gem5/ubuntu-24.04_all-dependencies:latest --outdir=ooo-stats/ run.py --processor_type=out-of-order
```

## Workload

The workload is a simple matrix multiply as shown below.

```cpp
for (int i = 0; i < size; i++) {
    for (int k = 0; k < size; k++) {
        for (int j = 0; j < size; j++) {
            C[i][j] += A[i][k] * B[k][j];
        }
    }
}
```

You can find the code in the `mm.cpp` file.

Two binaries are included in this directory:

- `mm`: An x86 binary which can be used for testing
- `mm-gem5`: An x86 binary with gem5 "magic" instructions which delineate the region of interest. You should use this binary with gem5.
- `mm-gem5-arm64`: An ARM64 binary with gem5 "magic" instructions which delineate the region of interest. You should use this binary with gem5.

### Using the workload in gem5

For arm:
```sh
gem5/build/ARM/gem5.opt scripts/run.py --processor_type a72 --bench scripts/workload/mm-gem5-arm64 --args 32
```

For x86:
```sh
gem5/build/X86/gem5.opt scripts/run.py --processor_type skylake --bench scripts/workload/mm-gem5 --args 32
```

By default when you run with the `run.py` script, some main statistics are printed on the terminal output.
If you want to see all of the detailed statistics you can find them in the `m5out/stats.txt` file.

### Building the workload

To compile the binary for your native machine, you can use `make mm`.

If you want to build the binary with the region of interest markers for gem5, you must first make sure that you have the gem5 source downloaded locally.
You will also have to ensure that the gem5 `m5` library is built.
To build the `m5` library, you can use the following command.

For x86:
```sh
cd gem5/util/m5
scons build/x86/out/libm5.a
```

For ARM:
```sh
cd gem5/util/m5
scons build/arm64/out/libm5.a
```

Then, to build `mm-gem5` you can use `make mm-gem5` (for x86) or `make mm-gem5-arm64` (for ARM).
You may need to pass the base gem5 directory with `make mm-gem5 GEM5_ROOT="<path to gem5>"`

## Downloading/building gem5

You can download gem5 from the gem5 git repository as shown below.

```sh
git clone https://github.com/gem5/gem5
```
To build gem5 you will need to install all dependencies and then build gem5.
See [the gem5 website](https://www.gem5.org/documentation/general_docs/building) for details.
Once you have the dependencies installed, you can use the following command.

```sh
scons -j`nproc` build/X86/gem5.opt
scons -j`nproc` build/ARM/gem5.opt
```
