# PySynic
Synthetic data generating framework for Python.

# Introduction

Creating synthetic data is domain specific but often there are common requirements. 
For example, you may want 
- numbers or dates that are anywhere within a range even if you don't care exactly where
- some values to be randomly null 
- a whole data frame to test your production code


PySynic facilitates that. 

However, what we're really advocating is the philosophy of creating synthetic data
to test your pipelines and machine learning models etc. 


If you find the code here helpful, then great. 
It's available on [PyPI](https://pypi.org/project/pysynic/) so just add `pysynic` to your dependency list.
It has no dependencies of its own so you won't have any transitive dependency issues.

# Example

You can use this framework to generate data for your tests. 
For instance, if you want to test PySpark code with 1000 rows of bespoke data, you could write something similar to:

```python
from pyspark.sql import SparkSession
from pysynic.synthetic_data import random_from, randomly_null, random_integer_in_range, random_date

def test_first_diagnosis(spark_session: SparkSession):
    data = []
    for i in range(1000):
        data.append([random_integer_in_range(0, 100, i),
                     randomly_null(random_from(["cancer", "heart attack", "stroke"])),
                     random_date(i, 31, "1/Jul/2021")
                     ])
    df = spark_session.createDataFrame(data, 
                                       ["patient_id", "disease_code", "admission_date"])
    results = YOUR_PRODUCTION_METHOD(df)
    assert results.count() > 0  # etc, etc
```
In this PyTest snippet, we create a Spark `DataFrame` that contains synthetic data.
We're not too interested in exactly what the data is, just that it is representative.
Then we use it to call our production code that presumably does something interesting and 
finally we make some sensible assertions. 
These assertions will be domain specific and we can't tell you what they are 
but hopefully you can see that with just a few lines of Python we can have large, semi-random
test data sets.

Note that in this example, the data is the same every time we run it. 
If you want it to be unpredictable, then don't provide a seed to the PySynic methods 
(in this case above, don't pass `i` but instead `None`).
Whether you want an element of determinism or true randomness is up to you. 
There are arguments for both.

If we were to run the same code in a PySpark shell, we could see that the output looks something like:
```
>>> df.show()
+----------+------------+-------------------+                                   
|patient_id|disease_code|     admission_date|
+----------+------------+-------------------+
|         0|        null|2021-07-01 00:00:00|
|         1|        null|2021-07-02 00:00:00|
|         2|        null|2021-07-03 00:00:00|
|         3|      cancer|2021-07-04 00:00:00|
|         4|      stroke|2021-07-05 00:00:00|
|         5|        null|2021-07-06 00:00:00|
|         6|        null|2021-07-07 00:00:00|
|         7|heart attack|2021-07-08 00:00:00|
|         8|        null|2021-07-09 00:00:00|
|         9|        null|2021-07-10 00:00:00|
|        10|        null|2021-07-11 00:00:00|
|        11|        null|2021-07-12 00:00:00|
|        12|      cancer|2021-07-13 00:00:00|
|        13|      stroke|2021-07-14 00:00:00|
|        14|        null|2021-07-15 00:00:00|
|        15|heart attack|2021-07-16 00:00:00|
|        16|heart attack|2021-07-17 00:00:00|
|        17|      stroke|2021-07-18 00:00:00|
|        18|      cancer|2021-07-19 00:00:00|
|        19|      stroke|2021-07-20 00:00:00|
+----------+------------+-------------------+
only showing top 20 rows
```