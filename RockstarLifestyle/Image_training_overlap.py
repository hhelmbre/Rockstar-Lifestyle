import pandas as pd
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint
#from function files
from RockstarLifestyle import Image_training_circles
from RocstarLifestyle import Image_training_circles_and _rectangles

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
