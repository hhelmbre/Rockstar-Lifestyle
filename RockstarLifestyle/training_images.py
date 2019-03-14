import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#from function files
from RockstarLifestyle import Image_training_pixels
from RockstarLifestyle import Image_training_circles

#Function 1: Generates a inputed number of images with random white pixels on a black background
#Steps: set seed, create a loop through requested number of images creating the Pixels on the background
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays
def random_image_generator(n):
    """Generates a number of images with randomized white pixels on a black
background"""
    i=0
    j=0
    k=0
    imgarray = [] #sets up the output array
    for i in range(0, n): #begins the counter on number of images based on the input
        img = Image.new('L', [250, 250]) #creates a 250x250 pixel image
        draw = ImageDraw.Draw(img)
        np.random.seed(123+i) #creates reproducibility in randomness that changes with each iteration
        for j in range(0,img.size[0]): #Creates random starting points for pixels
            for k in range(0, img.size[0]):
                a = randint(0,50)+(3*j)
                b = randint(0,50)+(3*k)
                c = a+1
                d = b+1
                draw.ellipse([a,b,c,d], fill=255)
                k=k+randint(90,100) #creates random jumps in the counter
            j = j+randint(90,100)
        array = np.array(img) #saves the image as a numpy array
        imgarray.append(array) #adds new array to the list of arrays
    return imgarray

#Function 2: Counts the number of white pixels in the image and records that
#Steps: Sets the counters for the black and obj pixels, runs through each pixel in the image and determines if it is black or white and then records the count of said color
#Inputs: the image array produced in the image generatior and the index the arrays
#Outputs: the number of black pixels and how many objects or white pixel
def pixel_counter_single_image(array, array_index):
    """Counts the number of colored pixels for a single image"""
    black = 0 #sets the counter to 0
    obj = 0 #sets the counter to 0
    img = Image.fromarray(array[array_index]) #Takes an array and creates an
					      #image
    for pixel in img.getdata(): #cycles through the pixels in each image
        if pixel == 0:
            black += 1
        else:
            obj += 1
    print('object=' + str(obj) + ', black=' +str(black))
    return black, obj


#Function 3: Runs the previous pixel counter for all requested images
#Steps: runs through a for loop of the number of images that were intially generated and runs the pixel counter for single images for each one.
#Inputs: the image array generated in the image_generator_rectangles
#Outputs: pixel count which contains the index, the numbers of objects normalized for each one, the number of black pixels and the total pixels.
def pixel_counter_whole_array(array):
    """Counts the number of pixels for """
    i = 0
    pixel_count = pd.DataFrame(columns=['Index','Object', 'Black', 'Total']) #Creates dataframefor storing count data
    for i in range(0,len(array)): #counts through the 'images' in the given array
        array_index = i
        black, obj = Image_training_pixels.pixel_counter_single_image(array, array_index)
        total = black + obj #sums up the number of pixels counted. Image are 250x250 so total should be 62500
        pixel_count.loc[i] = [i, obj, black, total]
    return pixel_count

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

#Function 1: Generates a inputed number of images with random white circles and white rectangles on a black background.
#Steps: set seed, create a loop through requested number of images creating the cirles and rectangles, append array with np versions of the images.
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays
def image_generator_circles_and_rectangles(n):
    np.random.seed(127)
    i=0
    j=2
    k=2
    imgarray = []
    for i in range(0, n):
        img = Image.new('L', [250, 250]) #creates a 250x250 pixel image
        draw = ImageDraw.Draw(img)
        w = randint(20,50) #creates random line assignments for circles and rectangles
        x = randint(20,50)
        y = randint(9,40)
        z = randint(9,40)
        for k in range (2, 240, w):
            for j in range (2, 240, x):
                a = j
                b = k
                c = j+8
                d = k+8
                draw.ellipse([a,b,c,d], fill=255)
        for m in range (2, 240, y):
            for n in range (2, 240, z):
                e = m
                f = n
                g = m+4
                h = n+4
                draw.rectangle([e,f,g,h], fill=255)
        array = np.array(img) #saves the image as a numpy array
        imgarray.append(array) #adds a callable feature for arrays
    return imgarray
