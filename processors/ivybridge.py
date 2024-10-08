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

# Ivy Bridge

class SBPort0(FUDesc):
    opList = [
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatSqrt", opLat=14, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=5, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=14, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdFloatDiv", opLat=14, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=14, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=25, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=5, pipelined=True)
    ]
    count = 1


class SBPort1(FUDesc):
    opList = [
        OpDesc(opClass="FloatAdd", opLat=3, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=3, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=5, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True)
    ]
    count = 1


class SBPort23(FUDesc):
    opList = [
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True)
    ]
    count = 2


class SBPort4(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1


class SBPort5(FUDesc):
    opList = [
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMisc", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True)
    ]
    count = 1


class SBExecUnits(FUPool):
    FUList = [SBPort0(), SBPort1(), SBPort23(), SBPort4(), SBPort5()]


class SBBranchPred(LTAGE):
    btb = SimpleBTB(numEntries=4096, tagBits=19)
    ras = ReturnAddrStack(numEntries=16)
    indirectBranchPred = IndirectPredIntel()

    tage = IntelTAGEBranchPredictor()

depth = 3
width = 4
class SBVerbatimCPU(DerivO3CPU):
    branchPred = SBBranchPred()

    # Pipeline delays
    # https://gem5-users.gem5.narkive.com/LNMJQ1M5/model-deeper-pipeline-in-x86#post2
    # to model 15 stage pipeline choose depth parameter as 3
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    iewToCommitDelay = 2*depth

    forwardComSize = 19
    backComSize = 19

    fuPool = SBExecUnits()

    # Pipeline widths
    fetchWidth = 4
    decodeWidth = 4
    renameWidth = 4
    dispatchWidth = 6
    issueWidth = 6
    wbWidth = 6
    commitWidth = 6
    squashWidth = 6

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