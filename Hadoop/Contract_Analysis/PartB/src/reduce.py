#!/usr/bin/env python

from operator import itemgetter
import sys
from datetime import datetime as dt

transactionCount = 0
contractsV = []
curr_key = None

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if curr_key == None:
        curr_key = key
    # buffer the value
    if curr_key == key:
        try:
            if value == "transaction":
                transactionCount += 1
            elif value == "true" :
                contractsV.append(value)
        except Exception as e:
            continue

    # We've read all the lines which have the same key
    else:
        try:
            if curr_key != None:
                if len(contractsV) > 0:
                    print "%s\t%d" % (curr_key,transactionCount)
            # update key
            curr_key = key
            # clean buffer
            transactionCount = 0
            contractsV = []
            # buffer the value
            try:
                if value == "transaction":
                    transactionCount += 1
                elif value == "true" :
                    contractsV.append(value)
            except Exception as e:
                continue
        except Exception as e:
            continue

# do not forget to output the last part if needed!
try:
    if curr_key == key:
        if len(contractsV) > 0:
            print "%s\t%d" % (curr_key,transactionCount)
except Exception as e:
    pass



