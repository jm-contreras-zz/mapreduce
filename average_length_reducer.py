#!/usr/bin/python

# Import relevant module
import sys

# Initialize empty lists
question_length = 0
answer_length = 0
answer_sum = 0
answer_count = 0

# Initialize an emtpy key
old_key = None	

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')

    # ...if it has three values
    if len(data) == 3:

      	# ...unpack them
      	new_key, node_type, body_length = data

    	# ...and if the new key differs from the old key (and if the old key has been set previously)
    	if new_key != old_key and old_key:
	    
    	    # ...compute the average answer length (if any answers exist)
    	    if answer_count > 0:
    		answer_length = float(answer_sum) / float(answer_count)

    	    # ...print the key-values pair
    	    print '{0}\t{1}\t{2}'.format(old_key, question_length, answer_length)
    
    	    # ...reset the lists
    	    question_length = 0
    	    answer_length = 0
    	    answer_sum = 0
    	    answer_count = 0

	# ...if the line is a question, determine its length
	if node_type == 'question':
	    question_length += int(body_length)
	# ...if the line is an answer, update the answer data
	elif node_type == 'answer':
	    answer_sum += int(body_length)
	    answer_count += 1

	# ...update the key
	old_key = new_key

# For the final line of the standard input...
if old_key != None:

    # ...compute the average answer length (if any answers exist)
    if answer_count > 0:
	answer_length = float(answer_sum) / float(answer_count)

    # ...print the key-values pair
    print '{0}\t{1}\t{2}'.format(old_key, question_length, answer_length)
