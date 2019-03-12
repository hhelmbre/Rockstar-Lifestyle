#imports of all required packages and python files
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
#code files that are within the tests
from RockstarLifestyle import Filter_Functions
from RockstarLifestyle import fouriertransform
from RockstarLifestyle import preprocessing

#Function 1: Test of high pass filter function from filter_functions
def test_high_pass_filter():
    """Test: takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
#inputs for the functions
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#function performance
    hpf_image = Filter_Functions.high_pass_filter(image, radius, desired_color) #runs the Function
#function asserts and checks
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input is the wrong form"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(hpf_image, np.ndarray), "output is the wrong form"
    return hpf_image

#Function 2: Test of HPF compare functions from filter_functions
def test_HPF_compare():
    """Test: Plots the image and the high pass filter image for comparison"""
#inputs for the functions
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#function performance
    Filter_Functions.HPF_compare(image, radius, desired_color)
#function asserts and checks
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input is the wrong form"
    #assert isinstance(image, Image.Image), "input is in the wrong form"
    return

#Function 3: Test of low pass filter function from filter_functions
def test_low_pass_filter():
    """Test: takes an image and modifiable radius and performs a fourier transform and outputs and image that has a low pass filter applied """
#function inputs
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#function performance
    lpf_image = Filter_Functions.low_pass_filter(image, radius, desired_color)
#function asserts and checks
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(lpf_image, np.ndarray), "output is in the wrong form"
    return lpf_image

#Function 4: Test of LPG compare functions from filter_functions
def test_LPF_compare():
    """Test: Plots the image and the low pass filter image for comparison"""
#input for function
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
#run function
    Filter_Functions.low_pass_filter(image, radius, desired_color)
#asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    return

#Function 5: Test of band pass filter functions from filter_functions
def test_band_pass_filter():
    """Test: takes an image and modifiable radii and performs a fourier transform and outputs and image that has a low pass filter applied"""
#function inputs
    image = Image.open('Test_Photo_fromMike.png')
    radiusin = 50
    radiusout = 100
    desired_color = "b"
#function performance
    bpf_image = Filter_Functions.band_pass_filter(image, radiusin, radiusout, desired_color)
#function asserts and checks
    assert isinstance(radiusin, int), "input is the wrong form"
    assert isinstance(radiusout, int), "input is the wrong form"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(bpf_image, np.ndarray), "output is in the wrong form"
    return

#Function 6: Test of BPF comparison function from filter_functions
def test_BPF_compare():
    """Test: Plots the image and the low pass filter image for comparison"""
#function Inputs
    image = Image.open('Test_Photo_fromMike.png')
    radiusin = 50
    radiusout = 100
    desired_color = "b"
#function performance
    Filter_Functions.BPF_compare(image, radiusin, radiusout, desired_color)
#asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    return
