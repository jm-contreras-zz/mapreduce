#!/usr/bin/python

# Import relevant module
import sys

# For every line in the data...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split(' ')
    
    # ...if it has 10 fields
    if len(data) == 10:
    
        # ...unpack them
        ip, identity, userid, time, zone, method, resource, protocol, status, size = data
        
        # ...print the key
        print '{0}'.format(resource)
