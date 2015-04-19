#!/usr/bin/env python

import sys

edge_a = 0
edge_b = 0
edge_c = 0

for line in sys.stdin:
    line = line.strip()
    
    x = len(line.split('\t'))
    
    if x == 3:
        edge_a, edge_c, edge_b = line.split('\t', 2)
    
    if x == 2:
        edge_a, edge_c = line.split('\t', 1)
    
    if x == 3:
        print("%s\t%s\t%s" % (edge_a, edge_c, edge_b))
    
    if x == 2:
        print("%s\t%s" % (edge_a, edge_c))