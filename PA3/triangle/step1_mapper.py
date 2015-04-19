#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    edge_a, edge_b = line.split("\t")    
    print("%s\t%s" % (edge_a, edge_b))