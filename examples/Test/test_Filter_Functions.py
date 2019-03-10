from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
import preprocessing

image = Image.open('Test_Photo_fromMike.png')
radius = 80
radiusin = 50
radiusout = 100


def test_high_pass_filter():
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    assert isinstance(radius, int)
    #assert isinstance(image, Image.fromarray), "input is the wrong form"
    hpf_image = Filter_functions.high_pass_filter(image, radius) #runs the Function
    assert isinstance(hpf_image, numpy.ndarray), "output is the wrong form"
    return hpf_image
#
# def test_HPF_compare(image, radius):
#     """Plots the image and the high pass filter image for comparison"""
#     high_pass_filter(image, radius)
#     return
#
# def test_low_pass_filter(image, radius):
#     """takes an image and modifiable radius and performs a fourier transform and outputs and image that has a low pass filter applied """
#     fourier_fshift(image)
#     assert isinstance(image, image), "input is the wrong form"
#     lpf_image = Filter_functions.py()
#     return lpf_im
#
# def test_LPF_compare(image, radius):
#     """Plots the image and the low pass filter image for comparison"""
#     low_pass_filter(image, radius)
#     return
#
# def test_band_pass_filter(image, radius):
#     """tests band pass filter function"""
#      band_pass_filter(image,radius)
#      return
