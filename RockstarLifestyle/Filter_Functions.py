#Purpose: create filters to go over images in an effort to extract infomation about them
#import external packages
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
#import internal packages
from RockstarLifestyle import fouriertransform, Filter_Functions, preprocessing

#Function 1: Performs a High Pass Filter and returns the modifed image
#Steps: fourier transform, creation of mask (define size, all ones, create zero circle, combine two), apply mask, shift back to image with mask applied
#Inputs: image and desired radius (used to change the starkness of the lines)
#Outputs: image that has been filtered
def high_pass_filter(image, radius, desired_color):
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
#forier transform the image and return fshift
    fshift = preprocessing.color_split_fshift(image, desired_color)

#building an array that covers the entire image as a mask
#determines the pixels in the rows and columns
    row, column = image.size
#the mask will be placed in the center so we need to know where the center is
    center_row = int(row/2)
    center_column = int(column/2)
    center = [center_row, center_column]
#for a HPF all other remaining values are one so we need to bulid an orginal array of all one in the size of the photograph
    ones_mask = np.ones((row, column))
#radius of the circle that is blocked out - can be changed to refine edges
    r=radius
#in order to create the circle of zeros we need to index an array of the same size as the image
    x, y = np.ogrid[:row,:column]
#equation of circle is x^2 + y^2 = r^2 - need to have a circle of zeros at the center of the image the less than fills the circle in to the origion
    zero_circle = (x - center_row) ** 2 + (y - center_column) ** 2 <= r*r
#now the last step to create the mask is the overlay the zero_circle on the ones mask
    ones_mask[zero_circle] = 0

#we still need to apply the mask to the fourier transform
    hpf_fshift = fshift * ones_mask
#now we need to revert the image array with mast applied back to a viewable image first with an inverse shift to move the componets to the correct locations
    hpf_revert = np.fft.ifftshift(hpf_fshift)
#then with a reverse forier transform
    hpf_image = np.fft.ifft2(hpf_revert)
#takes absolute value of the frequency
    hpf_image = np.abs(hpf_image)
    return hpf_image


#Function 2: Plotting the input image and the high pass filter image for comparison
#Steps: plots the input image, plot high pass filter image
#Input: input image and desired radius for filter mask
#Output: none it just shows the image for funsies
def HPF_compare(image, radius, desired_color):
    """Plots the image and the high pass filter image for comparison"""
    hpf_image = Filter_Functions.high_pass_filter(image, radius, desired_color)
#create subplot
    fig, axs = plt.subplots(1,2, figsize = (15,15))
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
#Steps: fourier transform, creation of mask (define size, all ones, create zero circle, combine two), apply mask, shift back to image with mask applied
#Inputs: image and desired radius (used to change the starkness of the lines)
#Outputs: image that has been filtered
def low_pass_filter(image, radius, desired_color):
    """takes an image and modifiable radius and performs a fourier transform and outputs and image that has a low pass filter applied """
#forier transform the image and return fshift
    fshift = preprocessing.color_split_fshift(image, desired_color)

#we will build an array that is covers the entire image as a mask
#determines the pixels in the rows and columns
    row, column = image.size
#the mask will be placed in the center so we need to know where the center is
    center_row = int(row/2)
    center_column = int(column/2)
    center = [center_row, center_column]
#for a LPF all other remaining values are zero so we need to bulid an orginal array of all zero in the size of the photograph
    zeros_mask = np.zeros((row, column))
#radius of the circle that is blocked out - can be changed to refine edges
    r=radius
#in order to create the circle of zeros we need to index an array of the same size as the image
    x, y = np.ogrid[:row,:column]
#equation of circle is x^2 + y^2 = r^2 - need to have a circle of ones at the center of the image- the less than fills the circle in to the origion
    ones_circle = (x - center_row) ** 2 + (y - center_column) ** 2 <= r*r
#now the last step to create the mask is the overlay the ones_circle on the zeros mask
    zeros_mask[ones_circle] = 1

# we still need to apply the mask to the fourier transform
    lpf_fshift = fshift * zeros_mask
#now we need to revert the image array with mask applied back to a viewable image first with an inverse shift to move the componets to the correct locations
    lpf_revert = np.fft.ifftshift(lpf_fshift)
#then with a reverse forier transform
    lpf_im = np.fft.ifft2(lpf_revert)
#takes absolute value of the frequency
    lpf_im = np.abs(lpf_im)
    return lpf_im


#Function 3: Plotting the input image and the low pass filter image for comparison
#Steps: plots the input image, plot low pass filter image
#Input: input image and desired radius for filter mask
#Output: none it just shows the image for funsies
def LPF_compare(image, radius):
    """Plots the image and the low pass filter image for comparison"""
    lpf_image = Filter_Functions.low_pass_filter(image, radius, desired_color)
#create subplot
    fig, axs = plt.subplots(1,2, figsize = (15,15))
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
#Steps: fourier transform, creation of mask (define size, all ones, create zero circle, combine two), apply mask, shift back to image with mask applied
#Inputs: image and desired internal and external radius (used to change the starkness of the lines), as well as the desired color from the color split
#Outputs: image that has been filtered
def band_pass_filter(image, radiusin, radiusout, desired_color):
    """takes an image and modifiable radii and performs a fourier transform and outputs and image that has a low pass filter applied """

#forier transform the image and return fshift
    fshift = preprocessing.color_split_fshift(image, desired_color)

#we will build an array that is covers the entire image as a mask
#determines the pixels in the rows and columns
    row, column = image.size
#the mask will be placed in the center so we need to know where the center is
    center_row = int(row/2)
    center_column = int(column/2)
    center = [center_row, center_column]
#radius of the circle that is blocked out - can be changed to refine edges
    r_in = radiusin
    r_out = radiusout
#in order to create the circle of zeros we need to index an array of the same size as the image
    x, y = np.ogrid[:row,:column]
#for a BPF all other remaining values are zero so we need to bulid an orginal array of all zero in the size of the photograph
    zeros_mask = np.zeros((row, column))
#equation of circle is x^2 + y^2 = r^2 - need to have a circle of ones at the center of the image- the less than fills the circle in to the origion
    ones_area = np.logical_and(((x - center_row) ** 2 + (y - center_column) ** 2 >= r_in ** 2), (x - center_row) ** 2 + (y - center_column) ** 2 <= r_out ** 2)
#now the last step to create the mask is the overlay the ones_area on the zeros mask
    zeros_mask[ones_area] = 1

# we still need to apply the mask to the fourier transform
    bpf_fshift = fshift * zeros_mask
#now we need to revert the image array with mask applied back to a viewable image first with an inverse shift to move the componets to the correct locations
    bpf_revert = np.fft.ifftshift(bpf_fshift)
#then with a reverse forier transform
    bpf_image = np.fft.ifft2(bpf_revert)
#takes absolute value of the frequency
    bpf_image = np.abs(bpf_image)
    return bpf_image

#Function 6: Plotting the input image and the band pass filter image for comparison
#Steps: plots the input image, plot band pass filter image
#Inputs: Image and desired internal and external radius (used to change the starkness of the lines), as well as the desired color from the color split
#Output: none it just shows the image for funsies
def BPF_compare(image, radiusin, radiusout, desired_color):
    """plots the band pass filter versus the input image"""
#gets the bpf image
    bpf_image = Filter_Functions.band_pass_filter(image, radiusin, radiusout, desired_color)
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
