#!/usr/bin/python

# Import relevant modules
import sys
import csv

# Load the data
reader = csv.reader(sys.stdin, delimiter='\t')

# Skip the header
reader.next()

# For every line in the data...
for line in reader:

    # ...that has 19 fields...
    if len(line) == 19:

    	# ...determine the node type (question, answer, or comment)
    	node_type = line[5]
    
    	# ...declare its key (as a function of node type) and print the key-values pair
    	if node_type == 'question':
    	    key = line[0]
    	elif node_type == 'answer' or node_type == 'comment':
    	    key = line[7]
    
        # ... print the key-value pair
        print '{0}\t{1}'.format(key, line[3])  # The value is author_id
