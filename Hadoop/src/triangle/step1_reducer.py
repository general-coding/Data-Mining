#!/usr/bin/env python

import sys

first = 0
edge_a = 0
current_edge_a = 0
edge_dict = {}
edge_list = []

for line in sys.stdin:
    try:
        line = line.strip()
 
        if first == 0:
            first = 1
            edge_a, edge_b = line.split('\t', 1)
            current_edge_a = edge_a
#             print(edge_a, edge_b)
        else:
            edge_a, edge_b = line.split('\t', 1)
#             print(edge_a, edge_b)
         
        if current_edge_a == edge_a:
            edge_list.append(edge_b)
            
        else:
            current_edge_a = edge_a
            edge_list = []
            edge_list.append(edge_b)     
            
        edge_dict[current_edge_a] = edge_list
#         print(edge_dict)
         
    except ValueError:
        break

# print(edge_dict)

for edge_a in edge_dict:
    try:
        l_edge_b = edge_dict[edge_a]
#        print('a%s\t%s\t' % (int(edge_a), l_edge_b))
        for edge_b in l_edge_b:
            try:
                l_edge_c = edge_dict[edge_b]
#                print('b\t%s\t%s' % (int(edge_b), l_edge_c))
#                 for edge in l_edge_c:
#                     print('%s\t%s\t%s' % (edge_a, edge, edge_b))
                for edge_c in l_edge_c:
                    try:
                        edge_x = edge_dict[edge_c]
                        for edge in edge_x:
                            if edge == edge_a and edge_c > edge_a and edge_b > edge_a:
                                print('%s\t%s\t%s\t%s' % (1, edge_a, edge_b, edge_c))
                    except KeyError:
                        pass
            except KeyError:
                pass
    except KeyError:
        pass