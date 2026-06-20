
from pyspark.sql.functions import *

column = ['Name','city','amount']
values = [('zeyo','chennai',500),('sai','bangalore',1000),('zeyo','hyd',200),('sai','bangalore',1000),('zeyo','chennai',500),('sai','bangalore',5000),('zeyo','chennai',500),('sai','Hyd',1000)]

df = spark.createDataFrame(values, column)

finaldf = df.groupBy("name").agg(sum("amount").alias("total"), count("amount").alias("count"),collect_list("amount").alias("list"))
#finaldf.show(10,False)

df.createOrReplaceTempView("table")

df = spark.sql("select name, sum(amount) as total, count(amount) as count, collect_list(amount) as list from table group by name").show(10,False)
------------------------------------------------------------------------------------------------------------------------------