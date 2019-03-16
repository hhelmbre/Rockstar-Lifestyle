#Purpose: For functions that perform pre-processessing of images
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
import scipy


#Function 1: Enhances the contrast on the image and produces an enhanced image
#Steps: converts an image to gray scale and inhances the contrast
#Input: image and desired contrast value
#Output: enhaced image
def image_contrast(image, contrast_value):
    """Increases the contrast of the image"""
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(contrast_value)
    return enhanced_image


#Function 2: Splits the image into rgb components preforms a forier transform
#Steps: split into rbg, use if tree to transform for desired color
#Input: desired color and image
#Output: desired color fshift
def color_split_fshift(image, desired_color):
    """splits the image into r or g or b color frequency then performs a fshift for that color"""
    image_color = Image.open('Test_Photo_fromMike.png')
    r,g,b = image_color.split()
    #if tree split based on desired color
    if desired_color == "b":
        f_blue = np.fft.fft2(b)
        fshift_blue = np.fft.fftshift(f_blue)
        m_spec_blue = np.log(np.abs(fshift_blue))
        fshift = fshift_blue
    elif desired_color == "g":
        f_green = np.fft.fft2(g)
        fshift_green = np.fft.fftshift(f_green)
        m_spec_green = np.log(np.abs(fshift_green))
        fshift = fshift_green
    elif desire_color == "r":
        f_red = np.fft.fft2(g)
        fshift_red = np.fft.fftshift(f_red)
        m_spec_red = np.log(np.abs(fshift_red))
        fshift = fshift_red
    #encompasses the rest of the inputs that do not work
    else:
         print('that desired color is not available')
    return(fshift)

#Function 3: Splits the image into rgb components
#Steps: split into components, used if tree create desired color image
#Input: desired color and image
#Output: desired color image
def color_split_image(image, desired_color):
    """splits the image into r or g or b color frequency then creates image with that color"""
    image_color = Image.open('Test_Photo_fromMike.png')
    r,g,b = image_color.split()
    #if tree split based on desired color
    if desired_color == "b":
        color_image = b
    elif desired_color == "g":
        color_image = g
    elif desire_color == "r":
        color_image = r
    #encompasses the rest of the inputs that do not work
    else:
         print('that desired color is not available')
    return(color_image)
