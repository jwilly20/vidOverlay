

# Parses the edf ascii format into a data structure

import sys

if (len(sys.argv) < 2):
	print "Usage: parser.py <filename.asc>"
	sys.exit()		# exit the program

ascFile = sys.argv[1]

print "Parsing file " + ascFile

f = open(ascFile)

print f

print f.readline()
