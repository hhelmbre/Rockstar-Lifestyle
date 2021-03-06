#Purpose: To test functions used for the multiresolution histogram
#Importing necessary packages
from PIL import Image, ImageFilter
import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy.ndimage import gaussian_filter
import timeit
#importing file functions
from rockstarlifestyle import multiresolution, preprocessing

#Function 3: Test of Gaussian Filter Application
def test_gauss_filter():
    """Test: Applies a Guassian Blur to all levels in list"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'g'
    image = preprocessing.color_split_image(image, desired_color)
    gauss_blur_list = [0,1] #function currently only works with two gauss blurs
    #function running
    gauss_blurs = multiresolution.gauss_filter(image, gauss_blur_list)
    #asserts and checks
    assert isinstance(desired_color, str), "intial input is wrong"
    assert isinstance(gauss_blur_list, list), "input is wrong"
    return gauss_blurs

#Function 4: Test of Obtaining histograms
def test_cumulative_hist():
    """Test: Creates a cumulative histogram through list"""
    #inputs for function
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'g'
    image = preprocessing.color_split_image(image, desired_color)
    gauss_blur_list = [0,1] #function currently only works with two gauss blurs
    gauss_blur_images = multiresolution.gauss_filter(image, gauss_blur_list)
    bin_list = [3] #number of bins desired for histogram
    #function running
    hist = multiresolution.cumulative_hist(gauss_blur_images, bin_list)
    #asserts and checks
    assert isinstance(gauss_blur_list, list), "input is wrong"
    return hist

#Function 5: Test for determining plot 1 and plot 2
def test_diff_plot_determination():
    """Test: Creates cumlative histograms and splits them into plot 1 and 2"""
    #inputs for function
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'g'
    #function currently only works with two gauss blurs
    gauss_blur_list = [0,1]
    bin_list = [3]
    #running the functions
    hist1_plot, hist2_plot = multiresolution.diff_plot_determination(
        image, desired_color, gauss_blur_list, bin_list)
    #asserts and checks
    return hist1_plot, hist2_plot

#Function 6: Test of obtianing difference histograms between two cumulative histograms
def test_diff_hist():
    """Test: Determines differences between two cumulative histogram"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'g'
    gauss_blur_list = [0,1] #function currently only works with two gauss blurs
    bin_list = [3]
    #getting the two plots needed to run difference
    hist1_plot, hist2_plot = multiresolution.diff_plot_determination(
        image, desired_color, gauss_blur_list, bin_list)
    #function running
    heights = multiresolution.diff_hist(hist1_plot, hist2_plot)
    #asserts and checks
    return heights
