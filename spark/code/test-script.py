from pyspark import SparkContext

sc = SparkContext()

rdd = sc.parallelize([100, 2, 3, 4, 5, 6, 7])
print("BLAHBLAHBLAH: "+str(rdd.take(1)))