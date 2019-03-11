import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint

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
        y = randint(9,50) #creates random jumps for the counter to have
			  #different patterns per image
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


def pixel_counter_single_image_rectangles(array, array_index):
    """Counts the number of pixels for individual rectangle images"""
    black = 0
    obj = 0
    img = Image.fromarray(array[array_index]) #converts image from array
					      #into an image
    for pixel in img.getdata(): #cycles through each pixel in the image
        if pixel == 0:
            black += 1
        else:
            obj += 1
    obj_normalized = obj/(25) #normalizes the number of pixels per square
    print('object=' + str(obj_normalized) + ', black=' +str(black))
    return



def pixel_counter_whole_array_rectangles(array):
    """Counts the number of pixels for the array of rectangle images"""
    i = 0
    pixel_count = pd.DataFrame(columns=['Index','Object','Black','Total'])
				#Creates dataframe for storing count data
    for i in range(0,len(array)): #counts through the 'images' in the given
				  #array
        img = Image.fromarray(array[i])
        black = 0
        obj = 0
        for pixel in img.getdata(): #counts pixels in each image
            if pixel == 0:
                black += 1
            else:
                obj += 1
        obj_normalized = obj/(25) #normalizes the number of pixels per
				  #square
        total = black + obj #sums up the number of pixels counted. Images
			    #are 250x250 so 62500 pixels should be counted.
        pixel_count.loc[i] = [i, obj_normalized, black, total] #updates the
						#dataframe with the counts
    return pixel_count
