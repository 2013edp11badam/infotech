#!/usr/bin/env python

import sys

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

for word in input_file.readline():
	print word[-2:]
	
