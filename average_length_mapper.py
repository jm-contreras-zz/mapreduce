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

        # ...determine its values
      	node_type = line[5]  # Node type (question, answer, or comment)
      	body_length = len(line[4])  # Body length

      	# ...declare its key (as a function of node type) and print the key-values pair
      	if node_type == 'question':
      	    key = line[0]
      	elif node_type == 'answer':
      	    key = line[6]

        # ... print the key-values pair for questions and answers
      	if node_type == 'question' or node_type == 'answer':
            print '{0}\t{1}\t{2}'.format(key, node_type, body_length)
