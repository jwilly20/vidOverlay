
'''
This is the main script for calling all other functions
'''

import sys
import parser
import Vision

# must pass a filename to parse
if (len(sys.argv) < 2):
	print "Usage: parser.py <filename.asc>"
	sys.exit()		# exit the program

# file we will parse
fileToParseName = sys.argv[1]

fixations = Vision.parseEDFASC(fileToParseName)


