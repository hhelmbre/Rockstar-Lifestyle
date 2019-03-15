import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#from function files
from RockstarLifestyle import training_images


#Function 1: Generates images with random pixels
#Steps: set seed, loops through images, and creates random white pixels
#Inputs: number of images
#Outputs: an array that has the images saved as numpy arrays

def rand_im_gen(n):
    """Generates images of random white pixels on black background"""
    i=0
    j=0
    k=0
    #sets up the output array
    imgarray = []
    #loops through images and pixel placement values
    for i in range(0, n):
	#creates a 250x250 pixel image
        img = Image.new('L', [250, 250])
        draw = ImageDraw.Draw(img)
	#creates reproducibility
        np.random.seed(123+i)
        for j in range(0,img.size[0]):
           for k in range(0, img.size[0]):
                a = randint(0,50)+(3*j)
                b = randint(0,50)+(3*k)
                c = a+1
                d = b+1
                draw.ellipse([a,b,c,d], fill=255)
	#creates random jumps in the counter
                k=k+randint(90,100)
            j = j+randint(90,100)
	#saves the image as a numpy array
        array = np.array(img)
	#adds new array to the list of arrays
        imgarray.append(array)
    return imgarray

#Function 2: Counts and records the number of white pixels in the image
#Steps: Set counters, parces through pixels, and record color of each
#Inputs: the image array from the image generator and its index
#Outputs: the number of black pixels and how many objects or white pixel

def pix_count_im(array, array_index):
    """Counts the number of colored pixels for a single image"""
    #sets all counters to 0
    black = 0
    obj = 0
    #Creates image from input array
    img = Image.fromarray(array[array_index])
    #Loops through the pixels in each image
    for pixel in img.getdata():
        if pixel == 0:
            black += 1
        else:
            obj += 1
    print('object=' + str(obj) + ', black=' +str(black))
    return black, obj


#Function 3: Runs the previous pixel counter for all requested images
#Steps: Loops through images and runs the pix_count_im
#Inputs: the image array generated in the image_generator_rectangles
#Outputs: dataframe containing index, circles, black pixels, and total

def pix_count_array(array):
    """Counts the number of pixels in each image of the array"""
    i = 0
    pixel_count = pd.DataFrame(columns=['Index','Object',
                                        'Black', 'Total'])
    #counts through the 'images' in given array
    for i in range(0,len(array)):
        array_index = i
        black, obj = training_images.pix_count_im(array, array_index)
        total = black + obj
        #sums up the pixels counted; should be 62500
        pixel_count.loc[i] = [i, obj, black, total]
    return pixel_count


#Function 4: Generates images with random circles on a black background
#Steps: set seed, loop through images creating the circles on background
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays

def im_gen_circles(n):
    """Generates a number of images with random circles"""
    #reproducible seed for randomness
    np.random.seed(125)
    i=0
    j=2
    k=2
    imgarray = []
    for i in range(0, n):
	#creates 250x250 image
	img = Image.new('L', [250, 250])
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
	#saves the image as a numpy array
	array = np.array(img)
	#adds a callable feature for array
	imgarray.append(array)
    return imgarray


#Function 5: Counts white pixels and translates that to circle count
#Steps: calls pix_count_im and normalizes it to circles
#Inputs: the image array from im_gen_circles and the index
#Outputs: the number of black pixels and number of circles

def pix_count_im_circles(array, array_index):
    """Counts the number of pixels for individual circle images"""
    black, obj = training_images.pix_count_im(array, array_index)
    #each full circle has 69 pixels in it
    obj_normalized = obj/(69)
    print('object=' + str(obj_normalized) + ', black=' +str(black))
    return black, obj_normalized

#Function 6: Runs the previous pixel counter for all requested images
#Steps: Loops through images and run index, circles, background, total. 
#Inputs: the image array from im_gen_circles
#Outputs: dataframe containing index, circles, black pixels, and total.

def pix_count_array_circles(array):
     """Counts the number of pixels for the array of circle images"""
     i = 0
    #Dataframe to fill with outputs
    pixel_count = pd.DataFrame(columns=['Index','Object',
                                        'Black','Total'])
    #loops through the images in the input array
    for i in range(0,len(array)):
	array_index = i
        black, obj_normalized = training_images.pix_count_im_circles(
                        	                  array, array_index)
	#62500 pixels total with 69 pixels per circle
	total = black + obj_normalized*69
        #updates dataframe
	pixel_count.loc[i] = [i, obj_normalized, black, total]
    return pixel_count


#Function 7: Generates images with random white rectangles on background
#Steps: set seed, loop through images creating the random rectangles
#Inputs: requested number of images
#Outputs: an array that has the images saved as numpy arrays

def im_gen_rect(n):
    """Generates images with random rectangles on background"""
    #Seeds the randomness for reproducibilitiy
    np.random.seed(126)
    i=0
    j=2
    k=2
    imgarray = []
    for i in range(0, n):
	#creates a 250x250 pixel image
	img = Image.new('L', [250, 250])
	draw = ImageDraw.Draw(img)
	#creates random patterning per image
	y = randint(9,50)
	z = randint(9,50)
	for k in range (2, 240, y):
	    for j in range (2, 240, z):
	    a = j
            b = k
	    c = j+4
	    d = k+4
	    draw.rectangle([a,b,c,d], fill=255)
	#saves the image as a numpy array
	array = np.array(img)
	#adds a callable feature for arrays
	imgarray.append(array)
    return imgarray


#Function 8: Counts number of rectangles in image
#Steps: calls pix_count_im and normalizes it to squares
#Inputs: the image array from im_gen_rect and the index the arrays
#Outputs: the number of black pixels and number of rectangles

def pix_count_im_rect(array, array_index):
    """Counts the number of pixels for individual rectangle images"""
    black, obj = training_images.pix_count_im(array, array_index)
    #25 pixels per rectangle
    obj_normalized = obj/(25)
    print('object=' + str(obj_normalized) + ', black=' +str(black))
    return black, obj_normalized


#Function 9: Runs the previous pixel counter for all requested images
#Steps: loops through images from im_gen_rect and runs pix_count_im 
#for each image
#Inputs: array from im_gen_rect
#Outputs: dataframe containing index, rectangles, black pixels and total

def pixel_counter_whole_array_rectangles(array):
    """Counts the number of rectangles per image"""
    i = 0
    array_index = 1
    #Dataframe for data storage
    pixel_count = pd.DataFrame(columns=['Index','Object',
                                        'Black','Total'])
    #loops through the images per array
    for i in range(0,len(array)):
        black, obj = training_images.pix_count_im_rect(
                                    array, array_index)
	array_index = i
	#There are 25 pixels per rectangle
	obj_normalized = obj/(25)
	#62500 pixels should be counted for each 250x250 image
	total = black + obj
	pixel_count.loc[i] = [i, obj_normalized, black, total]
    return pixel_count


#Function 10: Generates images with random white circles and rectangles.
#Steps: set seed, loops through images creating cirles and rectangles.
#Inputs: number of images
#Outputs: an array that has the images saved as numpy arrays

def im_genr_circles_and_rects(n):
    np.random.seed(127)
    i=0
    j=2
    k=2
    imgarray = []
    for i in range(0, n):
        #creates a 250x250 pixel image
        img = Image.new('L', [250, 250])
        draw = ImageDraw.Draw(img)
        #creates random shape patterning
        w = randint(20,50)
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
	#saves the image as a numpy array
        array = np.array(img)
	#adds a callable feature for arrays
        imgarray.append(array)
    return imgarray
