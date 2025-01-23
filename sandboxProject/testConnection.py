from pyspark.sql.functions import *
from pyspark.sql.types import *

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)
])

data = [(1, "John Doe"), (2, "Jane Doe"), (3, "Joe Bloggs")]

people = spark.createDataFrame(data, schema)
people.show()