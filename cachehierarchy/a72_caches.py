import m5
from m5.objects import (
    Cache,
    L2XBar,
    StridePrefetcher,
    WriteAllocator,
    SubSystem,
    TreePLRURP,
    PIFPrefetcher,
)
from m5.params import AddrRange, AllMemory, MemorySize
from m5.util.convert import toMemorySize


class CacheWalker(Cache):
    """Page Table Walker Cache.

    This cache is used by the MMU when a TLB miss occurs. The specification is
    not given by ARM, therefore we can refer to the HPI.py parameters and the
    Schaik et al. 'Reverse Engineering Hardware Page Table Caches Using
    Side-Channel Attacks on the MMU' paper.

    """

    # Find into the mentioned paper above.
    assoc = 4
    # Taken from the HPI.py. Correspond to the O3_ARM_v7a.py too.
    size = "1kB"  # The size have to correspond to 64 entries. Since we don't
    # know the size of an entry, we don't know what to set for the
    # size.
    data_latency = 4
    tag_latency = 4
    response_latency = 4
    mshrs = 6
    tgts_per_mshr = 8
    write_buffers = 16
    # Taken from the the O3_ARM_v7a.py.
    is_read_only = True

    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports


class L1ICache(Cache):
    """L1 Instruction cache.

    This private cache is used by one core to store
    instructions. Specifications are given in the architecture manual.

    """

    size = "48kB"
    assoc = 3
    data_latency = 1
    tag_latency = 1
    response_latency = 1
    mshrs = 2
    tgts_per_mshr = 8
    is_read_only = True

    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU icache port"""
        self.cpu_side = cpu.icache_port


class L1DCache(Cache):
    """L1 Data cache.

    This private cache is used by one core to store data. Specifications are
    given in the architecture manual.

    """

    size = "32kB"
    assoc = 2
    data_latency = 1
    tag_latency = 1
    response_latency = 1
    mshrs = 6
    tgts_per_mshr = 8
    write_buffers = 4
    prefetcher = StridePrefetcher(queue_size=4, degree=4)

    def connectBus(self, bus):
        """Connect this cache to a memory-side bus"""
        self.mem_side = bus.cpu_side_ports

    def connectCPU(self, cpu):
        """Connect this cache's port to a CPU dcache port"""
        self.cpu_side = cpu.dcache_port


class L2Cache(Cache):

    tag_latency = 12
    data_latency = 12
    response_latency = 12
    mshrs = 16
    tgts_per_mshr = 8
    size = "1MB"
    assoc = 16
    write_buffers = 8
    clusivity = "mostly_excl"
    # Simple stride prefetcher
    prefetcher = StridePrefetcher(degree=8, latency=1, prefetch_on_access=True)

    def connectCPUSideBus(self, bus):
        self.cpu_side = bus.mem_side_ports

    def connectMemSideBus(self, bus):
        self.mem_side = bus.cpu_side_ports
