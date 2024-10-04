
from m5.objects import DRAMInterface
from m5.objects import NVMInterface

class DDR4_2400_16x4(DRAMInterface):
    """
    A single DDR4-2400 x64 channel (one command and address bus), with
    timings based on a DDR4-2400 8 Gbit datasheet (Micron MT40A2G4)
    in an 16x4 configuration.

    Total channel capacity is 32GiB.

    16 devices/rank * 2 ranks/channel * 1GiB/device = 32GiB/channel
    """

    # size of device
    device_size = "1GiB"

    # 16x4 configuration, 16 devices each with a 4-bit interface
    device_bus_width = 4

    # DDR4 is a BL8 device
    burst_length = 8

    # Each device has a page (row buffer) size of 512 byte (1K columns x4)
    device_rowbuffer_size = "512B"

    # 16x4 configuration, so 16 devices
    devices_per_rank = 16

    # Match our DDR3 configurations which is dual rank
    ranks_per_channel = 2

    # DDR4 has 2 (x16) or 4 (x4 and x8) bank groups
    # Set to 4 for x4 case
    bank_groups_per_rank = 4

    # DDR4 has 16 banks(x4,x8) and 8 banks(x16) (4 bank groups in all
    # configurations). Currently we do not capture the additional
    # constraints incurred by the bank groups
    banks_per_rank = 16

    # override the default buffer sizes and go for something larger to
    # accommodate the larger bank count
    write_buffer_size = 128
    read_buffer_size = 64

    # 1200 MHz
    tCK = "0.833ns"

    # 8 beats across an x64 interface translates to 4 clocks @ 1200 MHz
    # tBURST is equivalent to the CAS-to-CAS delay (tCCD)
    # With bank group architectures, tBURST represents the CAS-to-CAS
    # delay for bursts to different bank groups (tCCD_S)
    tBURST = "3.332ns"

    # @2400 data rate, tCCD_L is 6 CK
    # CAS-to-CAS delay for bursts to the same bank group
    # tBURST is equivalent to tCCD_S; no explicit parameter required
    # for CAS-to-CAS delay for bursts to different bank groups
    tCCD_L = "5ns"

    # DDR4-2400 17-17-17
    tRCD = "14.16ns"
    tCL = "14.16ns"
    tRP = "14.16ns"
    tRAS = "32ns"

    # RRD_S (different bank group) for 512B page is MAX(4 CK, 3.3ns)
    tRRD = "3.332ns"

    # RRD_L (same bank group) for 512B page is MAX(4 CK, 4.9ns)
    tRRD_L = "4.9ns"

    # tFAW for 512B page is MAX(16 CK, 13ns)
    tXAW = "13.328ns"
    activation_limit = 4
    # tRFC is 350ns
    tRFC = "350ns"

    tWR = "15ns"

    # Here using the average of WTR_S and WTR_L
    tWTR = "5ns"

    # Greater of 4 CK or 7.5 ns
    tRTP = "7.5ns"

    # Default same rank rd-to-wr bus turnaround to 2 CK, @1200 MHz = 1.666 ns
    tRTW = "1.666ns"

    # Default different rank bus delay to 2 CK, @1200 MHz = 1.666 ns
    tCS = "1.666ns"

    # <=85C, half for >85C
    tREFI = "7.8us"

    # active powerdown and precharge powerdown exit time
    tXP = "6ns"

    # self refresh exit time
    # exit delay to ACT, PRE, PREALL, REF, SREF Enter, and PD Enter is:
    # tRFC + 10ns = 340ns
    tXS = "340ns"

    # Current values from datasheet
    IDD0 = "43mA"
    IDD02 = "3mA"
    IDD2N = "34mA"
    IDD3N = "38mA"
    IDD3N2 = "3mA"
    IDD4W = "103mA"
    IDD4R = "110mA"
    IDD5 = "250mA"
    IDD3P1 = "32mA"
    IDD2P1 = "25mA"
    IDD6 = "30mA"
    VDD = "1.2V"
    VDD2 = "2.5V"

class PCM_1200_16x4(DRAMInterface):
    """
    A single PCM-2400 x64 channel (one command and address bus), with
    timings based on a DDR4-2400 8 Gbit datasheet (Micron MT40A2G4)
    in an 16x4 configuration.
    Total channel capacity is 32GiB
    16 devices/rank * 2 ranks/channel * 1GiB/device = 32GiB/channel
    """

    # size of device
    device_size = "8GiB"

    # 16x4 configuration, 16 devices each with a 4-bit interface
    device_bus_width = 4

    # DDR4 is a BL8 device
    burst_length = 8

    # Each device has a page (row buffer) size of 512 byte (1K columns x4)
    device_rowbuffer_size = "512B"

    # 16x4 configuration, so 16 devices
    devices_per_rank = 16

    # Match our DDR3 configurations which is dual rank
    ranks_per_channel = 2

    # DDR4 has 2 (x16) or 4 (x4 and x8) bank groups
    # Set to 4 for x4 case
    bank_groups_per_rank = 4

    # DDR4 has 16 banks(x4,x8) and 8 banks(x16) (4 bank groups in all
    # configurations). Currently we do not capture the additional
    # constraints incurred by the bank groups
    banks_per_rank = 16

    # override the default buffer sizes and go for something larger to
    # accommodate the larger bank count
    write_buffer_size = 128
    read_buffer_size = 64

    # 1200 MHz
    tCK = "0.833ns"

    # 8 beats across an x64 interface translates to 4 clocks @ 1200 MHz
    # tBURST is equivalent to the CAS-to-CAS delay (tCCD)
    # With bank group architectures, tBURST represents the CAS-to-CAS
    # delay for bursts to different bank groups (tCCD_S)
    tBURST = "5ns"

    # @2400 data rate, tCCD_L is 6 CK
    # CAS-to-CAS delay for bursts to the same bank group
    # tBURST is equivalent to tCCD_S; no explicit parameter required
    # for CAS-to-CAS delay for bursts to different bank groups
    # ???
    tCCD_L = "10ns"

    # DDR4-2400 17-17-17
    tRCD = "55ns"
    tCL = "12.5ns"
    tRP = "14.16ns"
    tRAS = "32ns"

    # RRD_S (different bank group) for 512B page is MAX(4 CK, 3.3ns)
    tRRD = "3.332ns"

    # RRD_L (same bank group) for 512B page is MAX(4 CK, 4.9ns)
    tRRD_L = "4.9ns"

    # tFAW for 512B page is MAX(16 CK, 13ns)
    tXAW = "50ns"
    activation_limit = 4
    # tRFC is 350ns
    tRFC = "5ns"

    tWR = "150ns"

    # Here using the average of WTR_S and WTR_L
    tWTR = "5ns"

    # Greater of 4 CK or 7.5 ns
    tRTP = "7.5ns"

    # Default same rank rd-to-wr bus turnaround to 2 CK, @1200 MHz = 1.666 ns
    tRTW = "1.666ns"

    # Default different rank bus delay to 2 CK, @1200 MHz = 1.666 ns
    tCS = "1.666ns"

    # <=85C, half for >85C
    tREFI = "7.8us"

    # active powerdown and precharge powerdown exit time
    tXP = "6ns"

    # self refresh exit time
    # exit delay to ACT, PRE, PREALL, REF, SREF Enter, and PD Enter is:
    # tRFC + 10ns = 340ns
    tXS = "340ns"

class NVM_1200(NVMInterface):
    write_buffer_size = 128
    read_buffer_size = 64

    max_pending_writes = 128
    max_pending_reads = 64

    device_rowbuffer_size = "256B"

    # 8X capacity compared to DDR4 x4 DIMM with 8Gb devices
    device_size = "8GiB"
    # Mimic 64-bit media agnostic DIMM interface
    device_bus_width = 64
    devices_per_rank = 1
    ranks_per_channel = 1
    banks_per_rank = 16

    burst_length = 8

    two_cycle_rdwr = True

    # 1200 MHz
    tCK = "0.833ns"
    
    tREAD = "150ns"
    tWRITE = "500ns"
    tSEND = "14.16ns"
    # tBURST = "3.332ns"

    # Default all bus turnaround and rank bus delay to 2 cycles
    # With DDR data bus, clock = 1200 MHz = 1.666 ns
    tWTR = "1.666ns"
    tRTW = "1.666ns"
    tCS = "1.666ns"

    #tRCD = "55ns"
    #tXAW = "50ns"
    tBURST = "5ns"
    #tWR = "150ns"
    #tRFC = "5ns"
    #tCL = "12.5ns"
