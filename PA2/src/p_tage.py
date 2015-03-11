'''
Created on Mar 10, 2015

@author: puneeth
'''

import csv

result_path   = 'result_check.csv'
result_file = open(result_path,'r')
result_reader = csv.reader(result_file)

f1 = {}
for rows in result_reader:
    f1[rows[0]] = rows[1]


forest_path = 'pandababy6.csv'
forest_file = open(forest_path, 'r')
forest_reader = csv.reader(forest_file)

f2 = {}
for rows in forest_reader:
    f2[rows[0]] = rows[1]
    
x = len(set(f1.items()).intersection(set(f2.items())))

print(x)
print(x/565892)