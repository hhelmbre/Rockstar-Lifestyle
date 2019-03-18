#Purpose: create filters to go over images in an effort to extract 
#infomation 

#import external packages
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
#import internal packages
from rockstar_lifestyle import fouriertransform, edges, preprocessing

#Function 1: Performs a High Pass Filter and returns the modifed image
#Steps:fourier transform,create and apply mask, unshift and untransform
#Inputs: image, desired radius, desired color
#Outputs: image array of filtered image

def high_pass_filter(image, radius, desired_color):
    """Creates an image that has a high pass filter applied"""
    #Forier transform the image and return fshift.
    fshift = preprocessing.color_split_fshift(image, desired_color)
    #Build array that masks the entire image  
    #Circle of zeros in array of ones
    row, column = image.size
    center_row = int(row/2)
    center_column = int(column/2)
    ones_mask = np.ones((row, column))
    r=radius
    x, y = np.ogrid[:row,:column]
    zero_circle = (x - center_row) ** 2 + (y - center_column) ** 2 <= r*r
    ones_mask[zero_circle] = 0
    #Apply the mask to the fourier transform
    f_shift = fshift * ones_mask
    #Revert the masked image array back to a viewable image
    hpf_image = fouriertransform.inverse_fourier(f_shift)
    return hpf_image


#Function 2: Plots the input image and the hpf image for comparison
#Steps: plots the input image, plot high pass filter image
#Input: input image,desired radius for filter mask, desired color
#Output: none - shows figures

def HPF_compare(image, radius, desired_color):
    """Plots the image and the high pass filter image for comparison"""
    hpf_image = edges.high_pass_filter(image, radius, desired_color)
    #create subplot
    fig, axs = plt.subplots(1,2, figsize = (30,30))
    #plot input image
    ax = axs[0]
    ax.imshow(image)
    ax.set_title('Input')
    #plot high pass filter
    ax = axs[1]
    ax.imshow(hpf_image)
    ax.set_title('High Pass Filter')
    return


#Function 3: Performs a Low  Pass Filter and returns the modifed image
#Steps: fourier transform, create of mask, apply mask, inverse fourier
#Inputs: image, radius of circle in mask, desired color
#Outputs: filtered image array

def low_pass_filter(image, radius, desired_color):
    """Creates image with low pass filter applied"""
    #forier transform the image and return fshift
    fshift = preprocessing.color_split_fshift(image, desired_color)
    #Build an array that is covers the entire image as a mask
    row, column = image.size
    center_row = int(row/2)
    center_column = int(column/2)
    zeros_mask = np.zeros((row, column))
    r=radius
    x, y = np.ogrid[:row,:column]
    ones_circle = (x - center_row) ** 2 + (y - center_column) ** 2 <= r*r
    zeros_mask[ones_circle] = 1
    #Apply the mask to the fourier transform
    f_shift = fshift * zeros_mask
    #Revert the masked image array back with an inverse fourier transform
    lpf_image = fouriertransform.inverse_fourier(f_shift)
    return lpf_image


#Function 4: Plot and compare input image and the low pass filter image
#Steps: plots the input image and plots low pass filter image
#Input: input image and desired radius for filter mask
#Output: none, it just shows the image

def LPF_compare(image, radius, desired_color):
    """Plots the image and the low pass filter image for comparison"""
    lpf_image = edges.low_pass_filter(image, radius, desired_color)
    #create subplot
    fig, axs = plt.subplots(1,2, figsize = (30,30))
    #plot input image
    ax = axs[0]
    ax.imshow(image)
    ax.set_title('Input')
    #plot high pass filter
    ax = axs[1]
    ax.imshow(lpf_image)
    ax.set_title('Low Pass Filter')
    return


#Function 5: Performs a Band Pass Filter and returns the modifed image
#Steps: fourier transform, create mask, apply mask, 
# and then inverse fourier transform
#Inputs: image and desired internal and external radius, desired color
#Outputs: image that has been filtered

def band_pass_filter(image, radiusin, radiusout, desired_color):
    """Creates an image with band pass filter applied"""
    #forier transform the image and return fshift
    fshift = preprocessing.color_split_fshift(image, desired_color)
    #Build an array that is covers the entire image as a mask
    row, column = image.size
    center_row = int(row/2)
    center_column = int(column/2)
    center = [center_row, center_column]
    r_in = radiusin
    r_out = radiusout
    x, y = np.ogrid[:row,:column]
    zeros_mask = np.zeros((row, column))
    ones_area = np.logical_and(
        ((x - center_row) ** 2 + (y - center_column) ** 2 >= r_in ** 2),
        (x - center_row) ** 2 + (y - center_column) ** 2 <= r_out ** 2)
    zeros_mask[ones_area] = 1
    #Apply the mask to the fourier transform
    f_shift = fshift * zeros_mask
    #Inverse fourier transform
    bpf_image = fouriertransform.inverse_fourier(f_shift)
    return bpf_image

#Function 6: Plots and compares input image and band pass filter image
#Steps: plots the input image, plot band pass filter image
#Inputs: Image, desired internal and external radius, desired color
#Output: The image
def BPF_compare(image, radiusin, radiusout, desired_color):
    """plots the band pass filter versus the input image"""
    #gets the bpf image
    bpf_image = edges.band_pass_filter(image, radiusin, 
                                       radiusout, desired_color)
    #create subplot
    fig, axs = plt.subplots(1,2, figsize = (30,30))
    #plot input image
    ax = axs[0]
    ax.imshow(image)
    ax.set_title('Input')
    #plot high pass filter
    ax = axs[1]
    ax.imshow(bpf_image)
    ax.set_title('Band Pass Filter')
    return
