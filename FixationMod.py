

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
