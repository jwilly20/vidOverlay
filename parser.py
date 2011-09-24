

# Parses the edf ascii format into a data structure

import sys

class Fixation:
	'''
	Class for fixations - format taken directly from
	Eyelink II Head Monted User Manual 2.14.pdf section 4.9.3.4
	'''
	def __init__(self, eye, stime, etime, dur, axp, ayp, aps):
		self.eye = eye		# L for left, R for right
		self.stime = stime  # start time
		self.etime = etime 	# end time
		self.dur = dur		# duration
		self.axp = axp		# average x position
		self.ayp = ayp		# average y position
		self.aps = aps		# pupil size
		
	def __str__(self):
		return "{{ eye:{0} , stime: {1}, etime: {2}, dur: {3}, axp: {4}, ayp: {5}, aps: {6}}}".format(self.eye, self.stime, self.etime, self.dur, self.axp, self.ayp, self.aps)

# must pass a filename to parse
if (len(sys.argv) < 2):
	print "Usage: parser.py <filename.asc>"
	sys.exit()		# exit the program


# file we will parse
fileToParseName = sys.argv[1]
fileToParse = open(fileToParseName)
print "Parsing file " + fileToParseName

numFixations = 0
fixations = []

line = fileToParse.readline()
while (line != ''):
	splitLine = line.split(' ')	
	
	if (splitLine[0] == "EFIX"):
		numFixations += 1
		fixations.append(Fixation(splitLine[1], splitLine[2], splitLine[3], splitLine[4], splitLine[5], splitLine[6], splitLine[7]))
		print line ,

	line = fileToParse.readline()
# while end


print "\n\nNumber of fixations: " + str(numFixations/4)



