"""
This file defines a single core out of order processor for ARM.

The width, LSQ depth, and reorder buffer entries are parameterized. Other
configuration parameters have default values. See 
`gem5/src/cpu/o3/BaseO3CPU.py` for defaults
"""

from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from gem5.isas import ISA
from gem5.components.processors.cpu_types import CPUTypes

from processors.a72 import A72_Core_Layout


class A72Core(BaseCPUCore):
    """
    An out of order core for X86.
    The LSQ depth (split equally between loads and stores), the width of the
    core, and the number of entries in the reorder buffer are configurable.
    """

    def __init__(self, core_id):
        super().__init__(core=A72_Core_Layout(cpu_id=core_id), isa=ISA.ARM)


class A72ArmProcessor(BaseCPUProcessor):
    """
    A single core out of order processor for Arm.
    The LSQ depth (split equally between loads and stores), the width of the
    core, and the number of entries in the reorder buffer are configurable.
    """

    def __init__(self, cpu_type):
        self._cpu_type = CPUTypes.O3

        super().__init__(
            cores=[
                A72Core(
                    core_id=0,
                )
            ]
        )
