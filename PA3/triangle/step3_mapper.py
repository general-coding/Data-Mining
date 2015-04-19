#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    edge_a, count = line.split("\t", 1)
    
    print("%s\t%s" % (edge_a, count))
