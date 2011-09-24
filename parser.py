

# Parses the edf ascii format into a data structure

import sys

class Fixation:
	'''
	Class for fixations - format taken directly from
	Eyelink II Head Monted User Manual 2.14.pdf section 4.9.3.4
	'''
	def __init__(self, eye, stime, etime, dur, axp, ayp, aps):
		self.eye = eye		# string: L for left, R for right
		self.stime = stime  	# int: 	start time (msec timestamp)	
		self.etime = etime 	# int: end time   (msec)
		self.dur = dur		# int: duration
		self.axp = axp		# float: average x position
		self.ayp = ayp		# float: average y position
		self.aps = aps		# float: pupil size
		
	def __str__(self):
		return "{{ eye:{0} , stime: {1}, etime: {2}, \
				dur: {3}, axp: {4}, ayp: {5}, aps: {6}}}".format(self.eye, self.stime, 			\
										self.etime, self.dur, self.axp, self.ayp, self.aps)

# must pass a filename to parse
if (len(sys.argv) < 2):
	print "Usage: parser.py <filename.asc>"
	sys.exit()		# exit the program


# file we will parse
fileToParseName = sys.argv[1]
fileToParse = open(fileToParseName)
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



