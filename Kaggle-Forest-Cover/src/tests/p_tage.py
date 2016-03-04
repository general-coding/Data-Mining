'''
Created on Mar 10, 2015

@author: puneeth
'''

import csv

result_path   = './csvfiles/result_check.csv'
result_file = open(result_path,'r')
result_reader = csv.reader(result_file)

f1 = {}
for rows in result_reader:
    f1[rows[0]] = rows[1]

def per_tage(input_path):
    forest_path = './csvfiles/' + input_path
    forest_file = open(forest_path, 'r')
    forest_reader = csv.reader(forest_file)
    
    f2 = {}
    for rows in forest_reader:
        f2[rows[0]] = rows[1]
        
    x = len(set(f1.items()).intersection(set(f2.items())))
    
    print(x)
    print(x/565892)

# print('Accuracy forest_cover.csv')
# per_tage('forest_cover.csv')
# print('Accuracy pandababy1.csv')
# per_tage('pandababy1.csv')
# print('Accuracy pandababy2.csv')
# per_tage('pandababy2.csv')
# print('Accuracy pandababy3.csv')
# per_tage('pandababy3.csv')
# print('Accuracy pandababy4.csv')
# per_tage('pandababy4.csv')
# print('Accuracy pandababy5.csv')
# per_tage('pandababy5.csv')
# print('Accuracy pandababy6.csv')
# per_tage('pandababy6.csv')
# print('Accuracy pandababy7.csv')
# per_tage('pandababy7.csv')
print('Accuracy pandababy8.csv')
per_tage('pandababy8.csv')