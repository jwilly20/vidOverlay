
'''
This is the main script for calling all other functions
'''

import sys
import Vision
import dots

# must pass a filename to parse
if (len(sys.argv) < 2):
	print "Usage: main.py <filename.asc>"
	sys.exit()		# exit the program

# file we will parse
fileToParseName = sys.argv[1]

fixations = Vision.parseEDFASC(fileToParseName)

dots.drawFixationMovie(fixations, "image.jpg", 25)


