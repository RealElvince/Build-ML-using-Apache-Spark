from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ELT Pipeline") \
    .getOrCreate()


file_path = "data/ML_Data.parquet"

airbnb_df = spark.read.parquet(file_path)

airbnb_df.show(10)