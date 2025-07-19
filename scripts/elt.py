from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ELT Pipeline") \
    .getOrCreate()