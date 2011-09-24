

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
	color	- (r,g,b) tuple of fill color of circle
	'''
	
	drawInst.ellipse((center[0] - radius, center[1] - radius) + (center[0] + radius, center[1] + radius), fill=color)


def drawFixations(fixations, imageFile):
	'''
	fixations - a list of Fixation objects
	imageFile - filename of the image we will overlay the fixations onto

	Draws fixations as circles over the image file 
	'''
	dotColor = (255,0,0)
	im = Image.open(imageFile)

	draw = ImageDraw.Draw(im)

	while (len(fixations) != 0):
		current = fixations.pop()
		drawCirc(draw, (int(current.axp), int(current.ayp)), 20, dotColor)

	im.save("overlay.jpg", "JPEG")

