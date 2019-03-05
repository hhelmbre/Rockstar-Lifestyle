#Purpose

from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline


#Function 1: Performs a High Pass Filter and returns the modifed image
#Steps: fourier transform, creation of mask (define size, all ones, create zero circle, combine two), apply mask, shift back to image with mask applied
#Inputs: image and desired radius (used to change the starkness of the lines)
#Outputs: image that has been filtered
def high_pass_filter(image, radius):
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
#forier transform the image and return fshift
    fourier_fshift(image)

#building an array that covers the entire image as a mask
#determines the pixels in the rows and columns
    row, column = im.size
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
    hpf_revert = np.fft.ifftshift(hpf_fshift_blue)
#then with a reverse forier transform
    hpf_image = np.fft.ifft2(hpf_revert)
#takes absolute value of the frequency
    hpf_image = np.abs(hpf_im)
    return hpf_image


#Function 2: Plotting the input image and the high pass filter image for comparison
#Steps: plots the input image, plot high pass filter image
#Input: input image and desired radius for filter mask
#Output: none it just shows the image for funsies
def HPF_compare(image, radius):
    """Plots the image and the high pass filter image for comparison"""
    high_pass_filter(image, radius)
#create subplot
    fig, axs = plt.subplots(1,2, figsize = (15,15))
#plot input image
    ax = axs[0]
    ax.imshow(b)
    ax.set_title('Input')
#plot high pass filter
    ax = axs[1]
    ax.imshow(hpf_im)
    ax.set_title('High Pass Filter')
    return
