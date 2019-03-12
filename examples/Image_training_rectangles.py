import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#From function files
import Image_training_pixels
import Image_training_rectangles

#Function 1: Generates a inputed number of images with random white rectables on a black background
#Steps: set seed, create a loop through requested number of images creating the rectangles on the background
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays
def image_generator_rectangles(n):
	"""Generates a number of images with random rectangles on abackground"""
	np.random.seed(126) #Seeds the randomness for reproducibilitiy
	i=0
	j=2
	k=2
	imgarray = []
	for i in range(0, n):
		img = Image.new('L', [250, 250]) #creates a 250x250 pixel image
		draw = ImageDraw.Draw(img)
		y = randint(9,50) #creates random jumps for the counter to have different patterns per image
		z = randint(9,50)
		for k in range (2, 240, y):
			for j in range (2, 240, z):
				a = j
				b = k
				c = j+4
				d = k+4
				draw.rectangle([a,b,c,d], fill=255)
		array = np.array(img) #saves the image as a numpy array
		imgarray.append(array) #adds a callable feature for arrays
	return imgarray

#Function 2: Counts the number of white pixels in the image and translate that to number of objects
#Steps: calls the counting function defined in Image training pixels and then normalizes it to squares
#Inputs: the image array produced in the image generatior and the index the arrays
#Outputs: the number of black pixels and how many objects there are normalized
def pixel_counter_single_image_rectangles(array, array_index):
	"""Counts the number of pixels for individual rectangle images"""
	black, obj = Image_training_pixels.pixel_counter_single_image(array, array_index)
	obj_normalized = obj/(25) #normalizes the number of pixels per square
	print('object=' + str(obj_normalized) + ', black=' +str(black))
	return black, obj_normalized


#Function 3: Runs the previous pixel counter for all requested images
#Steps: runs through a for loop of the number of images that were intially generated and runs the pixel counter for single images for each one.
#Inputs: the image array generated in the image_generator_rectangles
#Outputs: pixel count which contains the index, the numbers of objects normalized for each one, the number of black pixels and the total pixels.
def pixel_counter_whole_array_rectangles(array):
	"""Counts the number of pixels for the array of rectangle images"""
	i = 0
	array_index = 1
	pixel_count = pd.DataFrame(columns=['Index','Object','Black','Total']) #Creates dataframe for storing count data
	for i in range(0,len(array)): #counts through the 'images' in the given array
		black, obj = Image_training_rectangles.pixel_counter_single_image_rectangles(array, array_index)
		array_index = i
		obj_normalized = obj/(25) #normalizes the number of pixels per square
		total = black + obj #sums up the number of pixels counted. Images are 250x250 so 62500 pixels should be counted.
		pixel_count.loc[i] = [i, obj_normalized, black, total] #updates the dataframe with the counts
	return pixel_count
