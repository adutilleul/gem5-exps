# -*- coding: utf-8 -*-
# Copyright (c) 2020 The Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Jason Lowe-Power, Trivikram Reddy

import m5
from m5.objects import *
import math
from .intel import *

# SKL (Client)

class SKLPort0(FUDesc):
    opList = [
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatSqrt", opLat=12, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=12, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True)
    ]
    count = 1


class SKLPort1(FUDesc):
    opList = [
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True)
    ]
    count = 1


class SKLPort2(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True)
    ]
    count = 1


class SKLPort3(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True)
    ]
    count = 1


class SKLPort4(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1


class SKLPort5(FUDesc):
    opList = [
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMisc", opLat=1, pipelined=True)
    ]
    count = 1


class SKLPort6(FUDesc):
    opList = [
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True)
    ]
    count = 1


class SKLPort7(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1

class SKLExecUnits(FUPool):
    FUList = [SKLPort0(), SKLPort1(), SKLPort2(), SKLPort3(), SKLPort4(), SKLPort5(), SKLPort6(), SKLPort7()]

class SKLBranchPred(LTAGE):
    btb = SimpleBTB(numEntries=4096, tagBits=19)
    ras = ReturnAddrStack(numEntries=16)
    indirectBranchPred = IndirectPredIntel()

    tage = IntelTAGEBranchPredictor()

depth = 3
width = 4
class SKLVerbatimCPU(DerivO3CPU):
    branchPred = SKLBranchPred()

    # Pipeline delays
    # https://gem5-users.gem5.narkive.com/LNMJQ1M5/model-deeper-pipeline-in-x86#post2
    # to model 15 stage pipeline choose depth parameter as 3
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    iewToCommitDelay = 2*depth

    forwardComSize = 19
    backComSize = 19

    fuPool = SKLExecUnits()

    # Pipeline widths
    fetchWidth = 6
    decodeWidth = 6
    renameWidth = 6
    dispatchWidth = 8
    issueWidth = 8
    wbWidth = 8
    commitWidth = 8
    squashWidth = 8

    fetchBufferSize = 16
    numROBEntries = 224
    numIQEntries = 128 
    LQEntries = 72
    SQEntries = 56
    numPhysIntRegs = 180
    numPhysFloatRegs = 168

    LSQDepCheckShift = 0
    LFSTSize = 1024
    SSITSize = 1024

# SKX (Server)

class SKXPort0(FUDesc):
    opList = [
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=12, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="SimdFloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdFloatSqrt", opLat=12, pipelined=True)
    ]
    count = 1


class SKXPort1(FUDesc):
    opList = [
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True)
    ]
    count = 1


class SKXPort2(FUDesc):
    opList = [
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True)
    ]
    count = 1


class SKXPort3(FUDesc):
    opList = [
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True)
    ]
    count = 1


class SKXPort4(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1


class SKXPort5(FUDesc):
    opList = [
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="SimdMisc", opLat=1, pipelined=True)
    ]
    count = 1


class SKXPort6(FUDesc):
    opList = [
        OpDesc(opClass="IntDiv", opLat=102, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True)
    ]
    count = 1


class SKXPort7(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1

class SKXExecUnits(FUPool):
    FUList = [SKXPort0(), SKXPort1(), SKXPort2(), SKXPort3(), SKXPort4(), SKXPort5(), SKXPort6(), SKXPort7()]

depth = 3
class SKXVerbatimCPU(DerivO3CPU):
    branchPred = SKLBranchPred()

    # Pipeline delays
    # https://gem5-users.gem5.narkive.com/LNMJQ1M5/model-deeper-pipeline-in-x86#post2
    # to model 15 stage pipeline choose depth parameter as 3
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    iewToCommitDelay = 2*depth

    forwardComSize = 19
    backComSize = 19

    fuPool = SKXExecUnits()

    # Pipeline widths
    fetchWidth = 6
    decodeWidth = 6
    renameWidth = 6
    dispatchWidth = 8
    issueWidth = 8
    wbWidth = 8
    commitWidth = 8
    squashWidth = 8

    fetchBufferSize = 16
    numROBEntries = 224
    numIQEntries = 128 
    LQEntries = 72
    SQEntries = 56
    numPhysIntRegs = 180
    numPhysFloatRegs = 168

    LSQDepCheckShift = 0
    LFSTSize = 1024
    SSITSize = 1024
