#!/usr/bin/env python

#Part B - Average Transaction Amount Per Day

import sys
import os
import string
from datetime import datetime as dt

# get the indexes for the attributes, matches them to keys and values
filename = os.environ.get("mapreduce_map_input_file")
transactions = "hash,nonce,transaction_index,from_address,to_address,value,gas,gas_price,receipt_cumulative_gas_used,receipt_gas_used,receipt_contract_address,receipt_root,receipt_status,block_timestamp,block_number"
transactions = transactions.split(',')
transactionsKeys = [transactions.index('block_timestamp')]
transactionValues = [transactions.index('value')]


# split the lines into a pair
for line in sys.stdin:
    if 'transactions_2019_11_01.csv' in filename:
        info = line.strip().split(',')
        if info[0] == 'hash':
            continue
        keys = list(info[i] for i in transactionsKeys)
        date = keys[0].split(" ")[0]
        values = list(info[i] for i in transactionValues)
        print '%s\t%s' % (date,values[0])


