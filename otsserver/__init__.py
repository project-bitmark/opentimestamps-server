# Copyright (C) 2017-2018 The OpenTimestamps developers
#
# This file is part of the OpenTimestamps Server.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of the OpenTimestamps Server including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.

from bitcoin.core import CoreChainParams
import os.path

__version__ = "0.3.0"

class BitmarkMainParams(CoreChainParams):
    NAME = "bitmarkmainnet"
    MAX_MONEY = 28000000*10**8
    GENESIS_BLOCK = None
    SUBSIDY_HALVING_INTERVAL = None
    PROOF_OF_WORK_LIMIT = None
    MESSAGE_START = b'\xf9\xbe\xb4\xd9'
    DEFAULT_PORT = 9265
    RPC_PORT = 9266
    DNS_SEEDS = (('bitmark.co','seed.bitmark.co'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':85,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :213}

class BitmarkTestnetParams(CoreChainParams):
    NAME = "bitmarktestnet"
    MAX_MONEY = 28000000*10**8
    GENESIS_BLOCK = None
    SUBSIDY_HALVING_INTERVAL = None
    PROOF_OF_WORK_LIMIT = None
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 19265
    RPC_PORT = 19266
    DNS_SEEDS = (('testnet.bitmark.co','seed.testnet.bitmark.co'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':130,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :258}

class BitmarkRegtestParams(CoreChainParams):
    NAME = "bitmarkregtest"
    MAX_MONEY = 28000000*10**8
    GENESIS_BLOCK = None
    SUBSIDY_HALVING_INTERVAL = None
    PROOF_OF_WORK_LIMIT = None
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 19266
    DNS_SEEDS = (('testnet.bitmark.co','seed.testnet.bitmark.co'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':130,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :258}
    
coin_conf_file = os.path.expanduser('~/.bitmark')
coin_conf_file = os.path.join(coin_conf_file,'bitmark.conf')
