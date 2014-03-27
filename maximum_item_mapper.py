#!/usr/bin/python

# Import relevant module
import sys

# For every line in the data...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')

    # ...if it has six values
    if len(data) == 6:

        # ...unpack them
        date, time, store, item, price, payment = data

        # ...print the key-value pair
        print '{0}\t{1}'.format(item, price)
