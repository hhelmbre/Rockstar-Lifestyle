import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#from function files
import Image_training_pixels
import Image_training_circles

#Function 1: Generates a inputed number of images with random white circles on a black background
#Steps: set seed, create a loop through requested number of images creating the circles on the background
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays
def image_generator_circles(n):
	"""Generates a number of images with random circles on a background"""
	np.random.seed(125) #creates the ability for the randomness to be reproducible
	i=0
	j=2
	k=2
	imgarray = []
	for i in range(0, n):
		img = Image.new('L', [250, 250]) #creates a 250x250 pixel image
		draw = ImageDraw.Draw(img)
		y = randint(9,50)
		z = randint(9,50)
		for k in range (2, 240, y):
			for j in range (2, 240, z):
				a = j
				b = k
				c = j+8
				d = k+8
				draw.ellipse([a,b,c,d], fill=255)
		array = np.array(img) #saves the image as a numpy array
		imgarray.append(array) #adds a callable feature for arrays
	return imgarray

#Function 2: Counts the number of white pixels in the image and translate that to number of objects
#Steps: calls the counting function defined in Image training pixels and then normalizes it to squares
#Inputs: the image array produced in the image generatior and the index the arrays
#Outputs: the number of black pixels and how many objects there are normalized
def pixel_counter_single_image_circles(array, array_index):
	"""Counts the number of pixels for individual circle images"""
	black, obj = Image_training_pixels.pixel_counter_single_image(array, array_index)
	obj_normalized = obj/(69) #each full circle has 69 pixels in it.
	print('object=' + str(obj_normalized) + ', black=' +str(black))
	return black, obj_normalized

#Function 3: Runs the previous pixel counter for all requested images
#Steps: runs through a for loop of the number of images that were intially generated and runs the pixel counter for single images for each one.
#Inputs: the image array generated in the image_generator_circles
#Outputs: pixel count which contains the index, the numbers of objects normalized for each one, the number of black pixels and the total pixels.
def pixel_counter_whole_array_circles(array):
	"""Counts the number of pixels for the array of circle images"""
	i = 0
	pixel_count = pd.DataFrame(columns=['Index','Object','Black','Total']) #Creates dataframe for storing count data
	for i in range(0,len(array)): #counts through the 'images' in the given array
		array_index = i
		black, obj_normalized = Image_training_circles.pixel_counter_single_image_circles(array, array_index)
		total = black + obj_normalized*69 #sums up the number of pixels counted. Images are 250x250 so 62500 pixels should be counted.
		pixel_count.loc[i] = [i, obj_normalized, black, total] #updates the dataframe with the counts
	return pixel_count
