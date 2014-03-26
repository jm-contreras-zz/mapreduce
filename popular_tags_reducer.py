#!/usr/bin/python

# Import relevant module
import sys

# Initialize an emtpy key, a key count, and a top-N list
old_key = None
key_count = 0
N = 10
topN_key = [None] * N
topN_value = [0] * N

# For every line in the standard input...
for line in sys.stdin:

    # ...strip it into a key
    new_key = line.strip()
    
    # ...if it consists of one value
    if new_key:

    	# ...and if the new key differs from the old key (and if the old key has been set previously)
    	if new_key != old_key and old_key:
    
    	    # ...find the smallest value in the top-N and its index
    	    min_count = min(topN_value)
    	    min_index = topN_value.index(min_count)
    
    	    # ...if the current value is larger, then update the top-N
    	    if key_count > min_count:
    		topN_key[min_index] = old_key
    		topN_value[min_index] = key_count
    
    	    # ...reset the key count
    	    key_count = 0

	# ...count it
	key_count += 1

	# ...update the key
	old_key = new_key

# For the final line of the standard input...
if old_key != None:

    # ...determine the sort order of the top-N
    so = sorted(range(N), key=lambda k: topN_value[k], reverse=True)

    # ...print the key-value pairs in sorted order
    for i in range(N):
	print '{0}\t{1}'.format(topN_key[so[i]], topN_value[so[i]])
