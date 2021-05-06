#!/usr/bin/env python
import sys

currentTerm = None
currentAmount = 0
currentCount = 0
for line in sys.stdin:
    key, amount = line.strip().split('\t')
    try:
        amount = int(amount)
    except Exception as e:
        continue
    if key == currentTerm:
        currentAmount+=amount
        currentCount+=1
    else:
        if currentTerm:
            print "%s\t%d" % (currentTerm,currentAmount/currentCount)
        currentTerm = key
        currentCount = 1
        currentAmount = amount

print "%s\t%d" % (currentTerm,currentAmount/currentCount) 

