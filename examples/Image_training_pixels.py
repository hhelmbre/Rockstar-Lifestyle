import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#from function files
import Image_training_pixels

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



def pixel_counter_whole_array(array):
    """Counts the number of pixels for """
    i = 0
    pixel_count = pd.DataFrame(columns=['Index','Object', 'Black', 'Total']) #Creates dataframefor storing count data
    for i in range(0,len(array)): #counts through the 'images' in the given array
        array_index = i
        black, obj = Image_training_pixels.pixel_counter_single_image(array, array_index)
        total = black + obj #sums up the number of pixels counted. Images
			    #are 250x250
        pixel_count.loc[i] = [i, obj, black, total]
    return pixel_count
