#!/usr/bin/python

# Import relevant module
import sys

# Declare the day of week (0 = Monday, 6 = Sunday)
day = 6

# Initialize sum and count variables
day_sum = 0.0
day_count = 0

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')
    
    # ...and if it has two values 
    if len(data) == 2:
    
        # ...unpack them
        this_day, this_sale = data
        
        # ...if the day is the same as the target day
        if int(this_day) == day:
            
            # ...add the sale to the sum and increase the count by 1
            day_sum += float(this_sale)
            day_count += 1

# For the final line of the standard input...
if day_count > 0:

    # ... print the day's mean sale
    print day_sum / day_count
