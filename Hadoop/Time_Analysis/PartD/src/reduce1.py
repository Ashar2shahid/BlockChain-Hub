#!/usr/bin/env python

from operator import itemgetter
import sys
from datetime import datetime as dt

transactionsV = []
contractsV = []
curr_key = None

for line in sys.stdin:
    key, value = line.strip().split('\t')
    values = value.split(',')
    if curr_key == None:
        curr_key = key
    # buffer the value
    if curr_key == key:
        try:
            if len(values) == 1:
                contractsV.append(value)
            elif len(values) == 2:
                transactionsV.append(value)
        except Exception as e:
            continue

    # We've read all the lines which have the same key
    else:
        if curr_key != None:
            if len(contractsV) > 0 and len(transactionsV) > 0:
                for transaction in transactionsV:
                    print "%s" % (transaction)
        # update key
        curr_key = key
        # clean buffer
        transactionsV = []
        contractsV = []
        # buffer the value
        try:
            if len(values) == 2:
                contractsV.append(values[0])
            elif len(values) == 1:
                transactionsV.append(values[0])
        except Exception as e:
            continue



# # do not forget to output the last part if needed!
# try:
#     if curr_key == key:
#         if len(contractsV) > 0 and len(transactionsV) > 0:
#             print "%s\t%d" % (contractsV[0],transactionsV[0])
# except Exception as e:
#     pass



