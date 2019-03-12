#Purpose: For functions that perform pre-processessing of images
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
import scipy


#Function 1: enhances the contrast on the image and produces and enhanced image
#Steps: creates an image from an image array - converts to gray scale and inhances the contrast
#Input: image array and desired contrast value
#Output: enhaced image
def im_contrast(image, contrast_value):
    img = Image.fromarray(image)
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    enhanced_im = enhancer.enhance(contrast_value)
    return enhanced_im


#Function 2: Splits the image into rgb components and creates shifts and magnitudes for them
#Steps: split into components, used inputs with if tree to create shifts and magnitude for desired color
#Input: desired color and image
#Output: desired color fshift
def color_split_fshift(image, desired_color):
    """splits the image into r or g or b color frequency then performs a fshift for that color"""
#splits the image into the rbg componetnts
    image_color = Image.open('Test_Photo_fromMike.png')
    r,g,b = image_color.split()
#if tree split based on desired color
    if desired_color == "b":
    #creates shift for blue
        f_blue = np.fft.fft2(b)
        fshift_blue = np.fft.fftshift(f_blue)
        m_spec_blue = np.log(np.abs(fshift_blue))
        fshift = fshift_blue
    elif desired_color == "g":
    #creates shift for green
        f_green = np.fft.fft2(g)
        fshift_green = np.fft.fftshift(f_green)
        m_spec_green = np.log(np.abs(fshift_green))
        fshift = fshift_green
    elif desire_color == "r":
    #creates shfit for red
        f_red = np.fft.fft2(g)
        fshift_red = np.fft.fftshift(f_red)
        m_spec_red = np.log(np.abs(fshift_red))
        fshift = fshift_red
    #encompasses the rest of the inputs that do not work
    else:
         print('that desired color is not available')
    return(fshift)

#Function 3: Splits the image into rgb components and creates the correct image coloring for them
#Steps: split into components, used inputs with if tree to create desired color image
#Input: desired color and image
#Output: desired color image
def color_split_image(image, desired_color):
    """splits the image into r or g or b color frequency then creates image with that color"""
#splits the image into the rbg componetnts
    image_color = Image.open('Test_Photo_fromMike.png')
    r,g,b = image_color.split()
#if tree split based on desired color
    if desired_color == "b":
    #names image for the desired color
        color_image = b
    elif desired_color == "g":
    #creates shift for green
        color_image = g
    elif desire_color == "r":
    #creates shfit for red
        color_image = r
    #encompasses the rest of the inputs that do not work
    else:
         print('that desired color is not available')
    return(color_image)
