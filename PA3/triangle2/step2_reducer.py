#!/usr/bin/env python

import sys

current_word = None
current_count = 0
current_combo = None
word = None
count = 0
combo = None
total = 0

for line in sys.stdin:
    try:
        line = line.strip()
        
        try:
            edge_a, edge_c, edge_b = line.split('\t', 2)
        except ValueError:
            edge_a, edge_c = line.split('\t', 1)
         
        combo = edge_a + '\t' + edge_c
         
        if current_combo == combo:
            current_count += 1
        else:
            if current_combo:
                print('%s\t%s' % (1, current_count))
             
            current_count = 0
            current_combo = combo
             
    except ValueError:
        pass
 
if current_combo == combo:
    print('%s\t%s' % (1, current_count))