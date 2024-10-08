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

# GLC (Alder Lake Perfomance)

class ADLPPort00(FUDesc):
    opList = [
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="SimdFloatSqrt", opLat=12, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=12, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=11, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=7, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True)
    ]
    count = 1


class ADLPPort01(FUDesc):
    opList = [
        OpDesc(opClass="IntDiv", opLat=18, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAdd", opLat=1, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=3, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=7, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True)
    ]
    count = 1


class ADLPPort02(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True)
    ]
    count = 1


class ADLPPort03(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True)
    ]
    count = 1


class ADLPPort04(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=12, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=12, pipelined=True)
    ]
    count = 1


class ADLPPort05(FUDesc):
    opList = [
        OpDesc(opClass="SimdFloatCmp", opLat=3, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=3, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=3, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMisc", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True)
    ]
    count = 1


class ADLPPort06(FUDesc):
    opList = [
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True)
    ]
    count = 1


class ADLPPort07(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=12, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=12, pipelined=True)
    ]
    count = 1


class ADLPPort08(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=12, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=12, pipelined=True)
    ]
    count = 1


class ADLPPort09(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=12, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=12, pipelined=True)
    ]
    count = 1


class ADLPPort10(FUDesc):
    opList = [
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True)
    ]
    count = 1


class ADLPPort11(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemRead", opLat=5, pipelined=True)
    ]
    count = 1



class ADLPExecUnits(FUPool):
    FUList = [ADLPPort00(), ADLPPort01(), ADLPPort02(), ADLPPort03(), ADLPPort04(), ADLPPort05(), ADLPPort06(), ADLPPort07(), ADLPPort08(), ADLPPort09(), ADLPPort10(), ADLPPort11()]

class ADLPBranchPred(LTAGE):
    btb = SimpleBTB(numEntries=16384, tagBits=19)
    ras = ReturnAddrStack(numEntries=16)
    indirectBranchPred = IndirectPredIntel()

    tage = IntelTAGEBranchPredictor()

depth = 3
width = 5
class GLCVerbatimCPU(DerivO3CPU):
    branchPred = ADLPBranchPred()

    # Pipeline delays
    # https://gem5-users.gem5.narkive.com/LNMJQ1M5/model-deeper-pipeline-in-x86#post2
    # to model 15 stage pipeline choose depth parameter as 3
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    iewToCommitDelay = 2*depth

    forwardComSize = 19
    backComSize = 19

    fuPool = ADLPExecUnits()

    # Pipeline widths
    fetchWidth = 8
    fetchBufferSize = 32
    decodeWidth = 8
    renameWidth = 8
    dispatchWidth = 12
    issueWidth = 12
    wbWidth = 12
    commitWidth = 12
    squashWidth = 12

    fetchBufferSize = 32
    numROBEntries = 512
    numIQEntries = 224
    LQEntries = 192
    SQEntries = 114
    numPhysIntRegs = 280
    numPhysFloatRegs = 332

    LSQDepCheckShift = 0
    LFSTSize = 1024
    SSITSize = 1024

