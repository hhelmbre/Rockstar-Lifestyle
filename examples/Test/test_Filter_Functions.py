from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import matplotlib as plt
import filter_functions
import fouriertransform

image = Image.open('Test_Photo_fromMike.png')
radius = 80



def test_high_pass_filter():
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
    hpf_image = filter_functions.high_pass_filter(image, radius, desired_color) #runs the Function
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input is the wrong form"
    assert isinstance(hpf_image, np.ndarray), "output is the wrong form"
    return hpf_image
#
# def test_HPF_compare(image, radius):
#     """Plots the image and the high pass filter image for comparison"""
#     high_pass_filter(image, radius)
#     return
#
def test_low_pass_filter():
    """tests low pass filter function """
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
    lpf_image = filter_functions.low_pass_filter(image, radius, desired_color)
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(lpf_image, np.ndarray), "output is in the wrong form"
    return lpf_image
#
# def test_LPF_compare(image, radius):
#     """Plots the image and the low pass filter image for comparison"""
#     low_pass_filter(image, radius)
#     return
#
def test_band_pass_filter():
    """tests band pass filter function"""
    image = Image.open('Test_Photo_fromMike.png')
    radiusin = 50
    radiusout = 100#
    desired_color = "b"
    bpf_image = filter_functions.band_pass_filter(image, radiusin, radiusout, desired_color)
    assert isinstance(radius, int), "input is the wrong form"
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(bpf_image, np.ndarray), "output is in the wrong form"
    return
