#!/usr/bin/env python

import sys

current_word = None
current_count = 0
current_combo = None
word = None
combo = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	speaker, word, count = line.split('\t', 2)
	
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	combo = speaker + word
	#if current_word == word:
	if current_combo == combo:
		current_count += count
	else:
		if current_combo:
		#if current_word:
			# write result to STDOUT
			print('%s\t%s' % (current_word, current_count))
		current_count = count
		#current_word = word
		current_combo = combo

# do not forget to output the last word if needed!
if current_combo == combo:
#if current_word == word:
	#print('%s\t%s' % (current_word, current_count))
	print('%s\t%s' % (current_combo, current_count))
