import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from random import randint

#import function packages
from RockstarLifestyle import Image_training_circles
from RockstarLifestyle import Image_training_pixels
from RockstarLifestyle import Image_training_rectangles

# From Image Training Circles Function Folders:

#Function 1: Test of image generator for the circles
def test_image_generator_circles():
    """Test: Generates a number of images with random circles on a background"""
#function Inputs
    n = 2
#function performance
    imgarray = Image_training_circles.image_generator_circles(n)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 2: Test of the pixel counter for the circles
def test_pixel_counter_single_image_circles():
    """Test: Counts the number of pixels for individual circle images"""
#function Inputs
    n = 2
    array = Image_training_circles.image_generator_circles(n)
    array_index = 1
#function performance
    black, obj_normalized = Image_training_circles.pixel_counter_single_image_circles(array, array_index)
#checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    assert isinstance(black, int), "Output is the wrong form"
    #assert isinstance(obj_normalized, int), "Output is the wrong form"
    assert obj_normalized >= 1, "no objects were created"
    assert black + obj_normalized * 69 == 62500, "the total number of objects (black pixels plus white pixels) is not correct"
    return

#Function 3: Test of the pixel counter for all arrays
def test_pixel_counter_whole_array_circles():
    """Test: Counts the number of pixels for the array of circle images"""
#function Inputs
    n = 2
    array = Image_training_circles.image_generator_circles(n)
#function performance
    pixel_count = Image_training_circles.pixel_counter_whole_array_circles(array)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    #assert pixel_count[1,1] + pixel_count[1,2]*69 == pixel_count[1,3], "the total is incorrect"
    #assert pixel_count[3] == 62500, "the total is incorrect"
    #assert isinstance(pixel_count, pd.Dataframe), "output is in the wrong form"
    return pixel_count


#From Image Training Pixels function filter
#Function 4
def test_random_image_generator():
    """Test: Generates a number of images with randomized white pixels on a black
background"""
    #function Inputs
    n = 2
    #function performance
    imgarray = Image_training_pixels.random_image_generator(n)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 4: Test of random pixel counter
def test_pixel_counter_single_image():
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
    assert obj >= 1, "no objects were created"
    assert black + obj == 62500, "the total number of objects (black pixels plus white pixels) is not correct"
    return black, obj


#Function 5: Test of random pixel counter for whole array
def test_pixel_counter_whole_array():
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
#Function 6: Test of image rectangle generator
def test_image_generator_rectangles():
    """Generates a number of images with random rectangles on abackground"""
#function Inputs
    n = 2
#function performance
    imgarray = Image_training_rectangles.image_generator_rectangles(n)
#checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(imgarray, list), "output is in the wrong form"
    return imgarray

#Function 7: Test of pixel counter for rectangles
def test_pixel_counter_single_image_rectangles():
    """Test: Counts the number of pixels for individual rectangle images"""
    #function Inputs
    n = 2
    array = Image_training_rectangles.image_generator_rectangles(n)
    array_index = 1
    #function performance
    black, obj_normalized = Image_training_rectangles.pixel_counter_single_image_rectangles(array, array_index)
    #checks and asserts
    assert isinstance(array_index, int), "Input is in the wrong form"
    assert isinstance(array, list), "Input is the wrong form"
    assert obj_normalized >= 1, "no objects were created"
    assert black + obj_normalized*25 == 62500, "the total number of objects (black pixels plus white pixels) is not correct"
    return black, obj_normalized


#Function 8: Test of pixel counter for every image requested
def test_pixel_counter_whole_array_rectangles():
    """Test: Counts the number of pixels for the array of rectangle images"""
    #function Inputs
    n = 2
    array = Image_training_rectangles.image_generator_rectangles(n)
    #function performance
    pixel_count =Image_training_rectangles.pixel_counter_whole_array_rectangles(array)
    #checks and asserts
    assert isinstance(n, int), "input is the wrong form"
    assert isinstance(array, list), "input is in the wrong form"
    return pixel_count
