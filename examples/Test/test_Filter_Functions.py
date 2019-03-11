#imports of all required packages and python files
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import matplotlib as plt
#code files that are within the tests
import filter_functions
import fouriertransform

#Function 1: Test of high pass filter function from filter_functions
def test_high_pass_filter():
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
#inputs for the functions
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#function performance
    hpf_image = filter_functions.high_pass_filter(image, radius, desired_color) #runs the Function
#function asserts and checks
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input is the wrong form"
    assert isinstance(hpf_image, np.ndarray), "output is the wrong form"
    return hpf_image
#
# def test_HPF_compare(image, radius):
#     """Plots the image and the high pass filter image for comparison"""
#     high_pass_filter(image, radius)
#     return

#Function 2: Test of low pass filter function from filter_functions
def test_low_pass_filter():
    """tests low pass filter function """
#function inputs
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#function performance
    lpf_image = filter_functions.low_pass_filter(image, radius, desired_color)
#function asserts and checks
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(lpf_image, np.ndarray), "output is in the wrong form"
    return lpf_image
#
# def test_LPF_compare(image, radius):
#     """Plots the image and the low pass filter image for comparison"""
#     low_pass_filter(image, radius)
#     return

#Function 3: Test of band pass filter functions from filter_functions
def test_band_pass_filter():
    """tests band pass filter function"""
#function inputs
    image = Image.open('Test_Photo_fromMike.png')
    radiusin = 50
    radiusout = 100
    desired_color = "b"
#function performance
    bpf_image = filter_functions.band_pass_filter(image, radiusin, radiusout, desired_color)
#function asserts and checks
    assert isinstance(radiusin, int), "input is the wrong form"
    assert isinstance(radiusout, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(bpf_image, np.ndarray), "output is in the wrong form"
    return
