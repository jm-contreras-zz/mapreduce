#!/usr/bin/python

# Import relevant module
import sys

# Initialize term variables
term = 'fantastic'
term_count = 0
term_question_IDs = []

# For every line in the standard input...
for line in sys.stdin:

    # ...strip and split it
    data = line.strip().split('\t')
    
    # ...if it has two values
    if len(data) == 2:
    
        # ...unpack them
        question_ID, this_term = data
        
        # ...if the present term matches the target term
        if this_term.lower() == term:
        
            # ...increase the count by 1 and append the question ID to the list
            term_count += 1
            term_question_IDs.append(int(question_ID))
            
# Sort the list
term_question_IDs.sort()

# Print the key-value pair after the final line
print '{0}\t{1}'.format(term_count, term_question_IDs)
