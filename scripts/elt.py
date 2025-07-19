from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ELT Pipeline") \
    .getOrCreate()


file_path = "data/ML_Data.parquet"

airbnb_df = spark.read.parquet(file_path)

airbnb_df.select("neighbourhood_cleansed", "room_type","bedrooms","bathrooms","number_of_reviews","price").show(10)