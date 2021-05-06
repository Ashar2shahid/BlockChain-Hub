#!/usr/bin/env python
import sys

currentTerm = None
currentCount = 0
for line in sys.stdin:
    key, count = line.strip().split('\t')
    try:
        count = int(count)
    except Exception as e:
        continue
    if key == currentTerm:
        currentCount+=count
    else:
        if currentTerm:
            print "%s\t%d" % (currentTerm,currentCount)
        currentTerm = key
        currentCount = count

print "%s\t%d" % (currentTerm,currentCount) 

