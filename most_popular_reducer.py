#!/usr/bin/python

# Import relevant module
import sys

# Initialize an empty key
old_key = None

# Initialize counters
max_hits = 0
current_count = 0

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')
 
    # ...if it has two values

    if len(data) == 2:

	# ...unpack them
	this_key, this_value = data

    	if old_key and old_key != this_key:
	    if (current_count > max_hits):
	    	max_hits = current_count
	    	top_path = old_value
            current_count = 0
	
    	old_key = this_key
    	old_value = this_value
    	current_count += 1
	
# For the final line of the standard input...
if old_key:
    if (current_count > max_hits):
		max_hits = current_count
		top_path = old_value

print '{0}\t{1}'.format(top_path, max_hits)

	


