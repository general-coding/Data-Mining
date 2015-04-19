#!/usr/bin/env python

import sys

total = 0

for line in sys.stdin:
        line = line.strip()

        edge, count = line.split('\t', 1)

        try:
                count = int(count)
        except ValueError:
                continue

        total = total + count
        
print(total)