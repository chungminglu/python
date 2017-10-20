from pyspark import SparkConf
from pyspark import SparkContext

SparkContext.setSystemProperty('spark.executor.memory', '10g')
SparkContext.setSystemProperty("spark.executor.cores",'4')

# sc = SparkContext("local[5]", "my pc 1")
sc = SparkContext("spark://nb.local:7077", "DeskTop11")

tmp = sc.textFile('/user/hsiung/data.csv')
# tmp = sc.textFile('d:/ddt.txt')

print(tmp.count())
# print(tmp.first())
# print(sc._conf.getAll())

# a=100
# b=200
# print(a+b)

SparkContext.stop(sc)
