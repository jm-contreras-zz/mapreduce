#!/usr/bin/python

# Import relevant module
import sys

# Initialize key and value
old_key = None
n_hits = 0

# For every line in the standard input...
for line in sys.stdin:

    # ...strip it
    this_key = line.strip()
    
    # ...if it contains one value
    if len(this_key) == 1:
    
        # ...and if the new key differs from the old key (and if the old key has been set previously)
        if old_key and old_key != this_key:
        
            # ...print the key-value pair
            print old_key, '\t', n_hits
            
            # ...reset the value
            n_hits = 0
    
        # ...update the key
        old_key = this_key
        
        # ...increase the value count
        n_hits += 1

# For the final line of the standard input...
if old_key != None:

    # ...print the key-value pair
    print old_key, '\t', n_hits
