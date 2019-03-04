#Purpose: To hold functions used for the multiresolution histogram

#Importing necessary packages
from PIL import Image, ImageFilter
import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy.ndimage import gaussian_filter
import MultiresHist as mult
import timeit

#Function 1: Importing images
def image_import():
    pass

#Function 2: Prepping the images
## Splits the image by color
##
def image_prep():
    pass

#Function 3: Gaussian Filter Application
#Input 1: the image that the filter will be applied
#Input 2: the list of gaussian blur levels that will be applied

#Functionality: applies a loop that goes through the gauss blur lists

#initializes the gauss_blurs list for appending later
gauss_blurs = []
def gauss_filter(image, gauss_blur_list):
    for levels in gauss_blur_list:
        gauss_blur = gaussian_filter(image, sigma=levels)
        gauss_blurs.append(gauss_blur)
    return gauss_blurs

#Function 4: Function for creating empty lists for each gaussian blur applied


#Function 5: Obtaining Histograms
#need to have variable bins functionality as well
hist = []
def cumulative_hist(gauss_blur_images, bin_list):
    for images in gauss_blur_images:
        for bin_count in bin_list:
            fig = plt.figure()
            hist_itt = plt.hist(images, bins=bin_count, density = True, cumulative = True)
            hist.append(hist_itt)
    return hist

#Function 6: Obtaining difference histograms between two cumulative histograms
heights = []
def diff_hist(hist1_plot, hist2_plot):
    bins1 = hist1_plot[0]
    bins2 = hist2_plot[0]
    bins = len(bins1)

    for i in range(bins):
        array1 = bins1[i]
        array2 = bins2[i]
        array_length = len(array1)
        heights_bins = []
        for j in range(array_length):
            bin1 = array1[j]
            bin2 = array2[j]
            height = bin1 - bin2
            heights_bins.append(height)
            heights.append(heights_bins)
    return heights
