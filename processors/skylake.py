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

class SKXPort0(FUDesc):
    opList = [
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="SimAdd", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=76, pipelined=False),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="FloatSqrt", opLat=12, pipelined=False),
        OpDesc(opClass="SimdFloatDiv", opLat=11, pipelined=False),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="FloatDiv", opLat=11, pipelined=False),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatSqrt", opLat=12, pipelined=False),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True)
    ]
    count = 1


class SKXPort1(FUDesc):
    opList = [
        OpDesc(opClass="SimAdd", opLat=1, pipelined=True),
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="SimdFloatCmp", opLat=4, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="FloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="FloatCvt", opLat=6, pipelined=True),
        OpDesc(opClass="SimdFloatMult", opLat=4, pipelined=True),
        OpDesc(opClass="SimdFloatCvt", opLat=3, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=76, pipelined=False),
        OpDesc(opClass="SimdMult", opLat=5, pipelined=True),
        OpDesc(opClass="SimdFloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatAdd", opLat=4, pipelined=True),
        OpDesc(opClass="FloatCmp", opLat=4, pipelined=True)
    ]
    count = 1


class SKXPort2(FUDesc):
    opList = [
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1


class SKXPort3(FUDesc):
    opList = [
        OpDesc(opClass="MemRead", opLat=5, pipelined=True),
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="FloatMemRead", opLat=5, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
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
        OpDesc(opClass="SimdCmp", opLat=1, pipelined=True),
        OpDesc(opClass="SimdShift", opLat=2, pipelined=True),
        OpDesc(opClass="SimdAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True),
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="SimdMisc", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=76, pipelined=False)
    ]
    count = 1


class SKXPort6(FUDesc):
    opList = [
        OpDesc(opClass="IntAlu", opLat=1, pipelined=True),
        OpDesc(opClass="IntDiv", opLat=76, pipelined=False),
        OpDesc(opClass="IntMult", opLat=4, pipelined=True)
    ]
    count = 1


class SKXPort7(FUDesc):
    opList = [
        OpDesc(opClass="FloatMemWrite", opLat=1, pipelined=True),
        OpDesc(opClass="MemWrite", opLat=1, pipelined=True)
    ]
    count = 1


class ExecUnits(FUPool):
    FUList = [SKXPort0(), SKXPort1(), SKXPort2(), SKXPort3(), SKXPort4(), SKXPort5(), SKXPort6(), SKXPort7()]

class IndirectPred(SimpleIndirectPredictor):
    indirectSets = 128 # Cache sets for indirect predictor
    indirectWays = 4 # Ways for indirect predictor
    indirectTagSize = 16 # Indirect target cache tag bits
    indirectPathLength = 7 # Previous indirect targets to use for path history
    indirectGHRBits = 16 # Indirect GHR number of bits

class LTAGE_BP(LTAGE_TAGE):
    nHistoryTables = 12
    minHist = 4
    maxHist = 34
    tagTableTagWidths = [0, 7, 7, 8, 8, 9, 10, 11, 12, 12, 13, 14, 15]
    logTagTableSizes = [14, 10, 10, 11, 11, 11, 11, 10, 10, 10, 10, 9, 9]
    logUResetPeriod = 19

class BranchPred(LTAGE):
    btb = SimpleBTB(numEntries=128+4096, tagBits=19) # L0 BTB + L1 BTB
    ras = ReturnAddrStack(numEntries=16)
    indirectBranchPred = IndirectPred() # use NULL to disable

    tage = LTAGE_BP()

depth = 3
width = 4
class SkylakeVerbatimCPU(DerivO3CPU):
    """ Uncalibrated: Configured based on micro-architecture documentation """

    branchPred = BranchPred()

    # Pipeline delays
    # https://gem5-users.gem5.narkive.com/LNMJQ1M5/model-deeper-pipeline-in-x86#post2
    # to model 15 stage pipeline choose depth parameter as 3
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    iewToCommitDelay = 2* depth

    forwardComSize = 19
    backComSize = 19

    fuPool = ExecUnits()

    # Pipeline widths
    fetchWidth = width
    decodeWidth = width
    renameWidth = 2*width
    dispatchWidth = 2*width
    issueWidth = 2*width
    wbWidth = 2*width
    commitWidth = 2*width
    squashWidth = 2*width

    fetchBufferSize = 16
    fetchQueueSize = 50 # 2 * 25
    numROBEntries = 224
    numIQEntries = 97 # 2 * 64
    LQEntries = 72
    SQEntries = 56
    numPhysIntRegs = 180
    numPhysFloatRegs = 168

depth = 3
width = 4
class SkylakeTunedCPU(DerivO3CPU):
    """ Calibrated: configured to match the performance of hardware """

    branchPred = BranchPred()

    # Pipeline delays
    fetchToDecodeDelay = depth
    decodeToRenameDelay = 1
    renameToIEWDelay = 3*depth
    issueToExecuteDelay = 1
    iewToCommitDelay = 2*depth

    forwardComSize = 19
    backComSize = 19

    # Pipeline widths
    fetchWidth = width * 2
    decodeWidth = width * 2
    renameWidth = 3*width
    issueWidth = 2*width
    dispatchWidth = 2*width
    wbWidth = 2*width
    commitWidth = 2*width
    squashWidth = 3*width

    fuPool = ExecUnits()
    # IntDiv()
    fuPool.FUList[0].opList[1].opLat = 2
    # IntMult()
    fuPool.FUList[1].opList[1].opLat = 2
    # Load
    fuPool.FUList[2].count = 12
    # store
    fuPool.FUList[4].count = 12
    fuPool.FUList[6].count = 3

    fetchBufferSize = 16
    fetchQueueSize = 64
    numROBEntries = 336
    numIQEntries = 146
    LQEntries = 72 * 2
    SQEntries = 56 * 2
    numPhysIntRegs = 270
    numPhysFloatRegs = 252