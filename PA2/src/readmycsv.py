'''
Created on Mar 6, 2015

@author: puneeth
'''

import csv

train_dict={}
ifname = 'train.csv'
ofname = 'train_data.csv'
count = 0
  
with open(ifname, 'r') as csvfile:
    fileDialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
    csvfile.seek(0)
    dictReader = csv.DictReader(csvfile, dialect=fileDialect)
    for row in dictReader:
        print(type(row))
        print(row)
        print(row['Id'])
        count = count + 1
        if count == 2:
            break;