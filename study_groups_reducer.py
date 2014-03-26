#!/usr/bin/python

# Import relevant module
import sys

# Initialize empty lists
author_list = []

# Initialize an emtpy key
old_key = None	

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')

    # ...if it has two values
    if len(data) == 2:

      	# ...unpack them and reformat body length as numeric
      	new_key, author_id = data
      
      	# ...and if the new key differs from the old key (and if the old key has been set previously)
      	if new_key != old_key and old_key:
      
      	    # ...print the key followed by the author ID list
      	    print '{0}\t{1}'.format(old_key, author_list)
      
      	    # ...reset the author ID list
      	    author_list = []

  	# ...append the current author ID to the author ID list
  	author_list.append(author_id)
  	
  	# ...update the key
  	old_key = new_key

# For the final line of the standard input...
if old_key != None:

    # ...print the key followed by the author ID list
    print '{0}\t{1}'.format(old_key, author_list)
