# -*- coding: utf-8 -*-
from pyspark import SparkConf
from pyspark import SparkContext

from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
import requests
import json

SparkContext.setSystemProperty('spark.executor.memory', '10g')
SparkContext.setSystemProperty("spark.executor.cores",'4')

class SparkHiveExample:

    def __init__(self):
        ## initialize spark session
        self.spark = SparkSession.builder.appName("Spark Hive example").enableHiveSupport().getOrCreate()

    def run(self):
        ## download with opendata API
        url = "http://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvTravelFood.aspx?"
        data = requests.get(url)

        ## convert from JSON to dataframe
        df = self.spark.createDataFrame(data.json())

        ## display schema
        df.printSchema()

        ## creates a temporary view using the DataFrame
        df.createOrReplaceTempView("travelfood")

        ## save into Hive
        self.spark.sql("DROP TABLE IF EXISTS travelfood_hive")
        df.write.saveAsTable("travelfood_hive")

        ## use SQL
        sqlDF = self.spark.sql("SELECT * FROM travelfood_hive WHERE City == '屏東縣'")
        sqlDF.select("Name", "City", "Town", "Coordinate").show()

    def test(self):
    	#sc = SparkContext("local[5]", "my pc 1")
	sc = SparkContext("spark://nb.local:7077", "DeskTop11")
	tmp = sc.textFile('/user/hsiung/data.csv')
	tmp = sc.textFile('d:/ddt.txt')

	print(tmp.count())
	print(tmp.first())
	print(sc._conf.getAll())

if __name__ == "__main__":
    EXAMPLE = SparkHiveExample()
    # EXAMPLE.run()
    EXAMPLE.test()    
    SparkContext.stop(sc)

