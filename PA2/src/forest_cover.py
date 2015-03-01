'''
Created on Feb 22, 2015

@author: puneeth
'''

import csv

fname = "train.csv"
count  = 0

train_dict={}

with open(fname, 'r') as csvfile:
    fileDialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
    csvfile.seek(0)
    dictReader = csv.DictReader(csvfile, dialect=fileDialect)
    for row in dictReader:
#         print(type(row))
        print(row)
#         print(row['Id'])
        count = count + 1
        if count == 2:
            break;