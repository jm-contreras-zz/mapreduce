#!/usr/bin/python

# Import relevant modules
import sys
from datetime import datetime

# For every line in the data...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')
    
    # ...if it has six values
    if len(data) == 6:
        
        # ...unpack them
        date, time, store, item, cost, payment = data
        
        # ...declare the day of the week
	day = datetime.strptime(date, '%Y-%m-%d').weekday()
	   
	# ...print the key-value pair
        print '{0}\t{1}'.format(day, cost)
