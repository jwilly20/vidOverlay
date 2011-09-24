

# Draws dots on the screen based on fixations

import Image, ImageDraw
import sys


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

	im = Image.open(imageFile)

	draw = ImageDraw.Draw(im)

	drawCirc(draw, (600,600), 20, (255,0,0))

	im.save("yoyo.jpg", "JPEG")

