#!/usr/bin/python

# Import relevant module
import sys

# Initialize a maximum price and an old key
max_price = 0.0
old_key = None

# For every line in the standard input...
for line in sys.stdin:

    # ... strip and split it
    data = line.strip().split('\t')

    # ...if it has two values
    if len(data) == 2:

        # ...unpack them
        this_key, this_price = data

        # ...and if the new key differs from the old key (and if the old key has been set previously)
        if old_key and old_key != this_key:
        
            # ...print the key-value pair
            print old_key, '\t', max_price
            
            # ...reset the maximum price
            max_price = 0.0
    
        # ...update the key
        old_key = this_key
    
        # ...if the current price is larger than the maximum price
        if float(this_price) > max_price:
        
            # ...set the current price as the maximum price
            max_price = float(this_price)

# For the final line of the standard input...
if old_key != None:

    # ...print the key-value pair
    print old_key, '\t', max_price
