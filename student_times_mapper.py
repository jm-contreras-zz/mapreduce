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

        # ...declare a key and a value
        key = line[3]
        value = line[8].split(' ')[1].split(':')[0]  # Extract the hour from a datetime string

        # ... print the key-value pair
        print '{0}\t{1}'.format(key, value)
