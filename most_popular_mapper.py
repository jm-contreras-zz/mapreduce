#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) == 10:
		resource = data[6]
		file_name = resource.split('/')[-1]
        print '{0}\t{1}'.format(file_name, resource)
