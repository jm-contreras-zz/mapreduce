#!/usr/bin/python

# Import relevant module
import sys

# Initialize an empty key
old_key = None

# Initialize an empty array to store hour counts
hour_counts = [0] * 24

# Define a function to find the hour(s) with the most visits and print the key-value pair(s)
def print_key_value(old_key, hour_counts):

    # Find the hour(s) with the most visits
    hours_most_visits = [hour for hour, count in enumerate(hour_counts) if count == max(hour_counts)]

    # For each hour with the most visits...
    for hour in hours_most_visits:

	# ...print a key-value pair
        print '{0}\t{1}'.format(old_key, hour)

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')

    # ...if it has two values
    if len(data) == 2:

    	# ...unpack them and reformat the value as numeric
    	new_key, hour = data
    	hour = int(hour)
    
    	# ...and if the new key differs from the old key (and if the old key has been set previously)
    	if new_key != old_key and old_key:
    
    	    # ...find the hour(s) with the most visits and print the key-value pair(s)
    	    print_key_value(old_key, hour_counts)
    
    	    # ...reset the hour counts
    	    hour_counts = [0] * 24

    	# ...update the key and hour counts
    	old_key = new_key
    	hour_counts[hour] += 1

# For the final line of the standard input...
if old_key != None:

    # ...find the hour(s) with the most visits and print the key-value pair(s)
    print_key_value(old_key, hour_counts)
