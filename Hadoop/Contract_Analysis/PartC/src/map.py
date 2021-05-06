#!/usr/bin/env python

#Part B - Average Transaction Amount Per Day

import sys
import os
import string
from datetime import datetime as dt

# get the indexes for the attributes, matches them to keys and values
filename = os.environ.get("mapreduce_map_input_file")
transactions = "token_address,from_address,to_address,value,transaction_hash,log_index,block_timestamp,block_number"
transactions = transactions.split(',')
transactionsKeys = [transactions.index('token_address')]
transactionValues = []


# split the lines into a pair
for line in sys.stdin:
    if 'tokentransfers_2019_11_01.csv' in filename:
        info = line.strip().split(',')
        if info[0] == 'hash':
            continue
        keys = list(info[i] for i in transactionsKeys)
        print '%s\t%s' % (keys[0],"1")


