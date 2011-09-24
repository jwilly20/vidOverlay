
# Parses the edf ascii format into a data structure

import sys
from Vision import *	

def parseEDFASC(filename):
	'''
	filename - filename of EDF ASC file to parse

	For now, parses out a list of Fixation objects	
	'''

	# file we will parse
	
	fileToParse = open(filename)
	print "Parsing file " + fileToParseName

	fixations = []
	
	line = fileToParse.readline()
	while (line != ''):
		splitLine = line.split()	
			
		if (len(splitLine) != 0):
			if (splitLine[0] == "EFIX"):
				fix_eye   = splitLine[1]
				fix_stime = int(splitLine[2])
				fix_etime = int(splitLine[3])
				fix_dur	  = int(splitLine[4])
				fix_axp   = float(splitLine[5])
				fix_ayp   = float(splitLine[6])
				fix_aps   = float(splitLine[7])
				fixations.append(Fixation(fix_eye, fix_stime, fix_etime, fix_dur, fix_axp, fix_ayp, fix_aps))
				print line ,
	
		line = fileToParse.readline()
	# end while

	print "\n\nNumber of fixations: " + str(len(fixations)/2)

	return fixations
