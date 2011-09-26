

'''
Overlays dots on an image based on fixations from a list of Fixation objects
'''

import Image, ImageDraw
import sys
from Vision import *

def drawCirc(drawInst, center, radius, color):
	'''
	drawInst - ImageDraw.Draw instance
	center	- (x,y) tuple of center of circle (in pixels)
	radius	- int radius of circle
	color	- (r,g,b) tuple of outline color of circle

  draws a "color" outlined circle at "center" with radius "radius"
	'''
	
	drawInst.ellipse((center[0] - radius, center[1] - radius) + (center[0] + radius, center[1] + radius), outline=color)

def drawDot(drawInst, center, radius, color):
	'''
	drawInst - ImageDraw.Draw instance
	center	- (x,y) tuple of center of circle (in pixels)
	radius	- int radius of circle
	color	- (r,g,b) tuple of fill color of circle

  draws a "color" filled circle at "center" with radius "radius" 
	'''
	
	drawInst.ellipse((center[0] - radius, center[1] - radius) + (center[0] + radius, center[1] + radius), fill=color)


def drawFixations(fixations, imageFile):
	'''
	fixations - a list of Fixation objects
	imageFile - filename of the image we will overlay the fixations onto

	Draws fixations as circles over the image file 
	'''
	rightDotColor = (0,255,0)
	leftDotColor = (255,0,0)
	durScale = 0.05			# direct relation of fixation duration to circle radius
	
	
	im = Image.open(imageFile)

	draw = ImageDraw.Draw(im)

	while (len(fixations) != 0):
		current = fixations.pop()
		if (current.isRight()):
			drawCirc(draw, (int(current.axp), int(current.ayp)), int(durScale * current.dur), rightDotColor)
		if (current.isLeft()):
			drawCirc(draw, (int(current.axp), int(current.ayp)), int(durScale * current.dur), leftDotColor)

	im.save("overlay.jpg", "JPEG")

def drawFixationMovie(fixations, imageFile):
  '''
  fixations - list of Fixation objects
  imageFile - filename of the image we will overlay fixations onto
  '''

  rightDotColor = (0,255,0)	
  leftDotColor = (255,0,0)
  durScale = 0.05			# direct relation of fixation duration to circle radius	

  im = Image.open(imageFile)

  draw = ImageDraw.Draw(im)

  while (len(fixations) != 0):
    current = fixations.pop()
    if (current.isRight()):
      drawDot(draw, (int(current.axp), int(current.ayp)), int(durScale * current.dur), rightDotColor)
    if (current.isLeft()):
      drawDot(draw, (int(current.axp), int(current.ayp)), int(durScale * current.dur), leftDotColor)

  im.save("overlay.jpg", "JPEG")
  
def drawMovie(imageFile):
  '''
	fixations - a list of Fixation objects
	imageFile - filename of the image we will overlay the fixations onto

	Draws fixations as circles over the image file 
	Outputs sequence of image files as image001.jpg, image002.jpg, etc.
	
  Images can be converted to avi with the command
  ffmpeg -f image2 -i img%03d.jpg a.avi
  '''
  radius = 20
  im = Image.open(imageFile)
  draw = ImageDraw.Draw(im)

  drawDot(draw, (20,20), radius, (255,0,0))
  for i in range(1, 60):
    print i
    im.save("img" + "%03d" % i + ".jpg")
	  
  for i in range(60, 120):
    print i
    drawDot(draw, (100,100), radius, (255,0,0))
    im.save("img" + "%03d" % i + ".jpg")

