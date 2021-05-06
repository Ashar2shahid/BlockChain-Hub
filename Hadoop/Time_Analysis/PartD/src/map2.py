#!/usr/bin/env python

#Part B - Average Transaction Amount Per Day

import sys
import os
import string
from datetime import datetime as dt

# get the indexes for the attributes, matches them to keys and values
filename = os.environ.get("mapreduce_map_input_file")
transactions = "block_timestamp,gas"
transactions = transactions.split(',')
transactionsKeys = [transactions.index('block_timestamp')]
transactionValues = [transactions.index('gas')]



# split the lines into a pair
for line in sys.stdin:
    if 'timeAnalysisPartD1.txt' in filename:
        try:
            info = line.strip().split(',')
            print '%s\t%s' % (info[0].split(" ")[0],info[1])
        except Exception as e:
            pass


