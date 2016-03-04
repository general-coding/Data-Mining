#!/usr/bin/env python

import sys

count = 0
total = 0

for line in sys.stdin:
    try:
        line = line.strip()
         
        count, edge_a, edge_c, edge_b = line.split('\t', 3)
         
        total = total + int(count)
        
    except ValueError:
        pass
 
print('%s' % (total))