from __future__ import print_function

import sys
from csv import reader
from datetime import datetime
from pyspark import SparkContext

def returnDate(dateString):
    return dateString.split(" ")[0]

sc = SparkContext()

transactions = sc.textFile(sys.argv[1], 1)
transactions = transactions.mapPartitions(lambda x: reader(x))

contracts = sc.textFile(sys.argv[2], 1)
contracts = contracts.mapPartitions(lambda x: reader(x))

transactionKeyValuePair = transactions.map(lambda x: (x[14], x[6]))
contractsKeyValuePair = contracts.map(lambda x: (x[5], x[4]))

result = transactionKeyValuePair.join(contractsKeyValuePair)

resultNewKey = result.map(lambda x: (returnDate(x[1][1]), int(x[1][0]) )).reduceByKey(lambda x,y: x + y)

outputFile = resultNewKey.map(lambda x: str(x[0]) + '\t' + str(x[1]) )
outputFile.saveAsTextFile("TimeAnalysisPartD")

sc.stop()