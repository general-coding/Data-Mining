# The first thing to do is to import the relevant packages
# that I will need for my script, 
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call 
# csv.[function] or np.[function] first

import pandas
import pylab

# Open up the csv file in to a Python object
df = pandas.read_csv('../train.csv', header=0)

# print(df)
# 
# df.head(2)
# 
# print(type(df))
# 
# df.info()

# print(df.describe())

df['Id'].hist()
pylab.show()