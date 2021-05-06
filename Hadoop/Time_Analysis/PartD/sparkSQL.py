from __future__ import print_function

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys

spark = SparkSession.builder.appName("TimeAnalysisPartD1").config("spark.some.config.option","some-value").getOrCreate()

transactionsV = spark.read.format('csv').options(header='true', inferschema= 'true').load(sys.argv[1])
contractsV = spark.read.format('csv').options(header='true', inferschema= 'true').load(sys.argv[2])

transactionsV.createOrReplaceTempView("Transactions")
contractsV.createOrReplaceTempView("Contracts")

result = spark.sql("""
    SELECT 
        t.block_timestamp,t.gas
    FROM 
        Transactions t 
    JOIN 
        Contracts c
        ON 
            t.block_number==c.block_number
            AND
            t.to_address==c.address
    """)

result.select(format_string('%d\t%s, %d, %d, %s', result.block_timestamp, result.gas)).write.save("TimeAnalysisPartD1", format="text")
