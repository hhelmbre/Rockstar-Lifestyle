from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
import matplotlib as plt
import preprocessing
import filter_functions
import fouriertransform

image = Image.open('Test_Photo_fromMike.png')
radius = 80



# def test_high_pass_filter():
#     """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
#     image = Image.open('Test_Photo_fromMike.png')
#     radius = 80
#     filter_functions.high_pass_filter(image, radius) #runs the Function
#     fouriertransform.fourier_fshift(image)
#     assert isinstance(radius, int)
#     #assert isinstance(image, Image.fromarray), "input is the wrong form"
#
#     assert isinstance(hpf_image, numpy.ndarray), "output is the wrong form"
#     return hpf_image
#
# def test_HPF_compare(image, radius):
#     """Plots the image and the high pass filter image for comparison"""
#     high_pass_filter(image, radius)
#     return
#
def test_low_pass_filter():
    """takes an image and modifiable radius and performs a fourier transform and outputs and image that has a low pass filter applied """
    image = Image.open('Test_Photo_fromMike.png')
    radius = 80
    desired_color = "b"
    lpf_image = filter_functions.low_pass_filter(image, radius, desired_color)
    #fshift = fouriertransform.fourier_fshift(image)
    #assert isinstance(image, image), "input is the wrong form"
    return lpf_im
#
# def test_LPF_compare(image, radius):
#     """Plots the image and the low pass filter image for comparison"""
#     low_pass_filter(image, radius)
#     return
#
# def test_band_pass_filter(image, radius):
#     """tests band pass filter function"""
# image = Image.open('Test_Photo_fromMike.png')
#   radiusin = 50
#   radiusout = 100#
#   bfp_image = filter_funciton.band_pass_filter(image,radius)
#      return
