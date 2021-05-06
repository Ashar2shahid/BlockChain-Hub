#!/usr/bin/env python

#Part E - Average Difficulty Per Day

import sys
import os
import string
from datetime import datetime as dt

# get the indexes for the attributes, matches them to keys and values
filename = os.environ.get("mapreduce_map_input_file")
blocks = "timestamp,number,hash,parent_hash,nonce,sha3_uncles,logs_bloom,transactions_root,state_root,receipts_root,miner,difficulty,total_difficulty,size,extra_data,gas_limit,gas_used,transaction_count"
blocks = blocks.split(',')
blocksKeys = [blocks.index('timestamp')]
blocksValues = [blocks.index('difficulty')]


# split the lines into a pair
for line in sys.stdin:
    if 'blocks_2019_11_01.csv' in filename:
        info = line.strip().split(',')
        if info[0] == 'timestamp':
            continue
        keys = list(info[i] for i in blocksKeys)
        date = keys[0].split(" ")[0]
        values = list(info[i] for i in blocksValues)
        print '%s\t%s' % (date,values[0])


