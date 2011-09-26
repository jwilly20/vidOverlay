
'''
This is the main script for calling all other functions
'''

import sys, os
from Vision import *
import dots

def prependFile(fileToParseName, fixations):
  #################3333
  ####################33
  #################3

  '''
  Code for adding sync to edf asc file
  Can we convert asc to edf? I think we can.
  '''

  # check this out in data viewer


  # read the current contents of the file
  f = open(fileToParseName)
  text = f.read()
  f.close()
  # open a different file for writing
  f = open(fileToParseName + "-new", 'w')

  # msec/frame bucket size
  movieFPS = 18
  frameLength = 1000 / movieFPS     # just cut it off
  precision = 4
  scaledFrameLength = int(round(frameLength * pow(10,precision), 0))    # used for frame bucket allocation
      
  # make the first fixation have start time 0 and shift all other fixations appropriately
  timeStart = fixations[0].stime   # we assume the first fixation is the first listed - may be bad assumption
  shiftedFixations = map(lambda fix : Fixation(fix.eye, fix.stime - timeStart, fix.etime - timeStart, fix.dur, fix.axp, fix.ayp, fix.aps), fixations)
  lastTimeStamp = max( map(lambda fix: fix.etime, shiftedFixations) )
    
  frameBuckets = {}    # hash of frame index to list of fixations
    
  # initialize every bucket in frameBuckets as an empty list
  scaledLastTimeStamp = lastTimeStamp * pow(10,precision)
  finalBucket = scaledLastTimeStamp / scaledFrameLength

  vidFilePath = "a.avi"

  for i in range (1, finalBucket + 1):
    f.write("MSG " + str(timeStart + frameLength * (i-1)) +  " !V VFRAME " + str(i) + " 152 144 " + vidFilePath + "\n")

  # write the original contents
  f.write(text)
  f.close()
  # did everything work safely?
  # if we get here, we're probably safe
  #os.rename(fileToParseName + "~", fileToParseName)


###############################################
## Start of program


# must pass a filename to parse
if (len(sys.argv) < 2):
	print "Usage: main.py <filename.asc>"
	sys.exit()		# exit the program

# file we will parse
fileToParseName = sys.argv[1]

fixations = parseEDFASC(fileToParseName)


#dots.drawFixationMovie(fixations, "image.jpg", 25)    # original code

prependFile(fileToParseName, fixations)

