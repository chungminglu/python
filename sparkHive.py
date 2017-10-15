# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
import requests
import json

class SparkHiveExample:

    def __init__(self):
        ## initialize spark session
        self.spark = SparkSession.builder.appName("Spark Hive example").enableHiveSupport().getOrCreate()

    def run(self):
        ## download with opendata API
        url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=17"
        # url = "http://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvTravelFood.aspx?"
        # url = "http://data.coa.gov.tw/Service/OpenData/Resume/ResumeData_Plus.aspx"
        # url = "http://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx"
        data = requests.get(url)

        ## convert from JSON to dataframe
        df = self.spark.createDataFrame(data.json())

        ## display schema
        df.printSchema()

        ## creates a temporary view using the DataFrame
        df.createOrReplaceTempView("travelfood")

        ## save into Hive
        self.spark.sql("DROP TABLE IF EXISTS aaa")
        df.write.saveAsTable("aaa")

        # ## use SQL
        # # sqlDF = self.spark.sql("SELECT * FROM travelfood_hive WHERE City == '屏東縣'")
        # sqlDF = self.spark.sql("SELECT * FROM travelfood_hive")
        # sqlDF.select("Name", "City", "Town", "Coordinate").show()

if __name__ == "__main__":
    EXAMPLE = SparkHiveExample()
    EXAMPLE.run()

