#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    count, edge_a, edge_b, edge_c = line.split('\t', 3)
    
    print("%s\t%s\t%s\t%s" % (count, edge_a, edge_b, edge_c))