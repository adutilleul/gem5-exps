from gem5.isas import ISA
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.boards.simple_board import SimpleBoard

from cachehierarchy.two_level_cache_hierarchy import TwoLevelCacheHierarchy

from memory.single_channel_pcm import (
    SingleChannelPCM_2400,
)

from processor_arm import A72ArmProcessor


class SimpleARMBoard(SimpleBoard):
    def __init__(
        self,
        clock_frequency="1.5GHz",
        processor=SimpleProcessor(cpu_type=CPUTypes.TIMING, isa=ISA.ARM, num_cores=1),
        cache_hierarchy=TwoLevelCacheHierarchy(),
    ):
        memory = SingleChannelPCM_2400("8GiB")

        super().__init__(
            clk_freq=clock_frequency,
            processor=processor,
            memory=memory,
            cache_hierarchy=cache_hierarchy,
        )


class A72ARMBoard(SimpleARMBoard):
    def __init__(
        self,
        cpu_type="verbatim",
        l1dwritelatency=0,
        l1dmshr=2,
        l1dwb=2,
        l2mshr=2,
        l2dwb=2,
        l3mshr=2,
        l3wb=2,
    ):
        super().__init__(
            processor=A72ArmProcessor(cpu_type),
            cache_hierarchy=TwoLevelCacheHierarchy(),
        )
