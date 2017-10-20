# import os
# import sys

import findspark
findspark.init()

from pyspark import SparkContext

# sc = SparkContext(master="local[4]")
sc = SparkContext(master='spark://nb.local:7077')

# print(sc.master)
print(sc._conf.getAll())

# ===========================

import numpy as np

TOTAL = 1000000
dots = sc.parallelize([2.0 * np.random.random(2) - 1.0 for i in range(TOTAL)]).cache()
print("Number of random points:", dots.count())

stats = dots.stats()
print('Mean:', stats.mean())
print('stdev:', stats.stdev())