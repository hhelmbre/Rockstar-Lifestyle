import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint

#import function packages
import Image_training_circles
import Image_training_pixels
import Image_training_rectangles

# From Image Training Circles Function Folders:

def test_image_generator_circles():
    """Generates a number of images with random circles on a background"""
#function Inputs
    n = 2
#function performance
    imgarray = Image_training_circles.image_generator_circles(n)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

def test_pixel_counter_single_image_circles():
    """Counts the number of pixels for individual circle images"""
#function Inputs
    n = 2
    array = Image_training_circles.image_generator_circles(n)
    array_index = 1
#function performance
    Image_training_circles.pixel_counter_single_image_circles(array, array_index)
#checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    return

def test_pixel_counter_whole_array_circles():
    """Counts the number of pixels for the array of circle images"""
#function Inputs
    n = 2
    array = Image_training_circles.image_generator_circles(n)
#function performance
    pixel_count = Image_training_circles.pixel_counter_whole_array_circles(array)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    #assert isinstance(pixel_count, pd.Dataframe), "output is in the wrong form"
    return pixel_count


def test_function():
#function Inputs
#function performance
#checks and asserts
    return



#From Image Training Pixels function filter
def test_random_image_generator():
    """Generates a number of images with randomized white pixels on a black
background"""
    #function Inputs
    n = 2
    #function performance
    imgarray = Image_training_pixels.random_image_generator(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray


def pixel_counter_single_image():
    """Counts the number of colored pixels for a single image"""
    #function Inputs
    n = 2
    array = Image_training_pixels.random_image_generator(n)
    array_index = 1
    #function performance
    black, obj = Image_training_pixels.pixel_counter_single_image(array, array_index)
    #checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    return black, obj



def pixel_counter_whole_array(array):
    """Counts the number of pixels for """
#function Inputs
    n = 2
    array = Image_training_pixels.random_image_generator(n)
#function performance
    pixel_count = Image_training_pixels.pixel_counter_whole_array(array)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    return pixel_count




# From Image Training Rectangles
def image_generator_rectangles(n):
    """Generates a number of images with random rectangles on abackground"""
#function Inputs
    n = 2
#function performance
    imgarray = image_generator_rectangles.image_generator_rectangles(n)
#checks and asserts
    return imgarray


def pixel_counter_single_image_rectangles(array, array_index):
    """Counts the number of pixels for individual rectangle images"""
    #function Inputs
    n = 2
    array = image_generator_rectangles.image_generator_rectangles(n)
    array_index = 1
    #function performance
    black, obj_normalized = Image_training_rectangles.pixel_counter_single_image_rectangles(array, array_index)
    #checks and asserts
    return black, obj_normalized



def pixel_counter_whole_array_rectangles(array):
    """Counts the number of pixels for the array of rectangle images"""
    #function Inputs
    n = 2
    array = image_generator_rectangles.image_generator_rectangles(n)
    #function performance
    pixel_count =Image_training_rectangles.pixel_counter_whole_array_rectangles(array)
    #checks and asserts
    return pixel_count
