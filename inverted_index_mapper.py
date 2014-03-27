#!/usr/bin/python

# Import relevant modules
import sys
import csv
import re

# Load the data
reader = csv.reader(sys.stdin, delimiter='\t')

# For every line in the data...
for line in reader:

    # ...define the question ID and the question text
    question_ID = line[0]
    question_text = line[4]
    
    # ...for every term in the question text (parsing out non-term characters)
    for term in re.split(r'[,.!?:;"()<>\[\]#$=\-/\s]', question_text):
    
        # ...print the key-value pair
        print '{0}\t{1}'.format(question_ID, term)

