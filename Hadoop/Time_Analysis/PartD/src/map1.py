#!/usr/bin/env python

#Part B - Average Transaction Amount Per Day

import sys
import os
import string
from datetime import datetime as dt

# get the indexes for the attributes, matches them to keys and values
filename = os.environ.get("mapreduce_map_input_file")
transactions = "hash,nonce,transaction_index,from_address,to_address,value,gas,gas_price,receipt_cumulative_gas_used,receipt_gas_used,receipt_contract_address,receipt_root,receipt_status,block_timestamp,block_number"
contracts = "address,bytecode,is_erc20,is_erc721,block_timestamp,block_number"
transactions = transactions.split(',')
contracts = contracts.split(',')
transactionsKeys = [transactions.index('block_number'),transactions.index('to_address')]
transactionValues = [transactions.index('block_timestamp'),transactions.index('gas')]
contractKeys = [contracts.index('block_number'),contracts.index('address')]
contractValues = [contracts.index('is_erc20')]



# split the lines into a pair
for line in sys.stdin:
    if 'transactions_2019_11_01.csv' in filename:
        info = line.strip().split(',')
        if info[0] == 'hash':
            continue
        keys = list(info[i] for i in transactionsKeys)
        values = list(info[i] for i in transactionValues)
        print '%s\t%s' % (",".join(keys),",".join(values))

    elif 'contracts_2019_11_01.csv' in filename:
        info = line.strip().split(',')
        if info[0] == 'address':
            continue
        keys = list(info[i] for i in contractKeys)
        values = list(info[i] for i in contractValues)
        print '%s\t%s' % (",".join(keys),",".join(values))


