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

        # ...split the tag names by whitespace into a list
        tagnames = line[2].split(' ')

    	# ...and print each one as a key
    	for key in tagnames:
    	    print key
