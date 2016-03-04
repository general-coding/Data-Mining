#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	speaker, text = line.split(':', 1)
	stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
					'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
					'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
					'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 
					'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
					'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 
					'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
					'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 
					'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 
					'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 
					'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 
					'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
					'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
	# split the line into words
	words = re.findall(r"[\'A-Za-z]+", text)
	words = [word.lower() for word in words]
	words = [word for word in words if word not in stopwords]

	# increase counters
	for word in words:
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py
		#
		# tab-delimited; the trivial word count is 1
		print('%s\t%s\t%s' % (speaker, word, 1))
