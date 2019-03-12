#Purpose: Tests for preprocessing functions
#import external packages
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
import scipy
#import internal packages
from RockstarLifestyle import preprocessing
from RockstarLifestyle import fouriertransform

#Function 1: Test of im_contrast
def test_im_contrast():
#inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    contrast_value = 2
#function performance
    enhanced_im = preprocessing.im_contrast(image, contrast_value)
#asserts and checks
    return enhanced_im

#Function 2: Test of color_split_fshift
def test_color_split_fshift():
    """test of a function which splits the image into r or g or b color frequency then performs a fshift for that color"""
# inputs for the function
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
#function performance
    fshift = preprocessing.color_split_fshift(image, desired_color)
#asserts and checks
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(fshift, np.ndarray), "output is in the wrong form"
    return(fshift)

#Function 5: Test of color_split_image
def test_color_split_image():
    """test of a function which splits the image into r or g or b color frequency then performs a fshift for that color"""
# inputs for the function
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
#function performance
    color_image = preprocessing.color_split_image(image, desired_color)
#asserts and checks
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    #assert isinstance(color_image, Image.Image), "output is in the wrong form"
    return(color_image)
