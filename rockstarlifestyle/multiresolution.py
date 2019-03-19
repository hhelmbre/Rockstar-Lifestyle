#Purpose: To hold functions used for the multiresolution histogram

#Importing necessary packages
from PIL import Image, ImageFilter
import numpy as np
from numbers import Number
from matplotlib import pyplot as plt
import scipy
from scipy.ndimage import gaussian_filter
import timeit
import matplotlib.cbook as cbook
#import internal packages
from rockstarlifestyle import multiresolution, preprocessing


#Function 1: Importing images
def image_import():
    pass

#Function 2: Prepping the images
## Splits the image by color
##
def image_prep():
    pass

#Function 3: Gausian filter application
#Steps: uses for loop to apply a guassian blur to all levels in list
#Input: input image, gaussian blur list
#Output: creates the gauss blur list for later

def gauss_filter(image, gauss_blur_list):
    """Applies a Guassian Blur to all levels in list"""
    gauss_blurs = []
    for levels in gauss_blur_list:
        gauss_blur = gaussian_filter(image, sigma=levels)
        gauss_blurs.append(gauss_blur)
    return gauss_blurs


#Function 4: Obtaining Histograms
#Steps: cycles through images and bins to plot histogram and append to hist list
#Input: gaussian blured images, list of bins
#Output: list of histograms including one for each image for all bins
def cumulative_hist(gauss_blur_images, bin_list, show_figs = True):
    """Creates a cumulative histogram through list"""
    hist = []
    for images in gauss_blur_images:
        for bin_count in bin_list:
            if show_figs:
                fig = plt.figure()
                hist_itt = plt.hist(images, bins = bin_count,
                                   density = True, cumulative = True)
            else:
                hist_itt = nofig_cumulative_hist(images, bins = bin_count)
            hist.append(hist_itt)
    return hist

def nofig_cumulative_hist(x, bins):
    """
    The following function is based off the hist() class-based function within the
    _axes.py file of matplotlib located in:
    ...\matplotlib-base-3.0.3-py37h3e3dc42_0\Lib\site-packages\matplotlib\axes\_axes.py
    The current hist() method in matplotlib outputs figures along with data. The
    problem with this is that figures take computation time to execute and iterating
    this method over multiple datasets can cause crashing. At the same time,
    downstream functions require input data in a similar format as matplotlib
    function output. To resolve this, we use the hist() class function used in
    matplotlib and suppress the section of code that draws out the graphs and
    only output an array of the height-data and corresponding bins.

    Parameters
    ----------
    x : np.uint16 : List of datapoints to process
    bins : np.uint16 : String of bins to use in np.histogram()

    Return
    ------
    tops : np.array(dtype=float) : histogram heights
    bins : list : list of bin edges
    """
    tops = []
    x = cbook._reshape_2D(x, 'x')
    nx = len(x)
    xmin = np.inf
    xmax = -np.inf
    for xi in x:
        if len(xi) > 0:
            xmin = min(xmin, np.nanmin(xi))
            xmax = max(xmax, np.nanmax(xi))
    bin_range = (xmin, xmax)
    for i in range(nx):
        m, bins = np.histogram(x[i], bins, bin_range, density = True)
        m = m.astype(float)
        tops.append(m)
    slc = slice(None)
    tops = [(m * np.diff(bins))[slc].cumsum()[slc] for m in tops]
    return tops, bins



#Function 5: Determines plot 1 and 2 from initial image, blur list, and bin list
#Steps: load all input, run the cumulative_hist function, split into one and two
#Inputs: intial image, blur list and bin list
#Outputs: histogram plot one and two

def diff_plot_determination(image, desired_color, gauss_blur_list, bin_list):
    """Creates cumlative histograms and splits them into plot 1 and 2"""
    image = preprocessing.color_split_image(image, desired_color)
    gauss_blur_images = multiresolution.gauss_filter(image, gauss_blur_list)
    hist = multiresolution.cumulative_hist(gauss_blur_images, bin_list)
    hist1_plot = hist[0]
    hist2_plot = hist[1]
    return hist1_plot, hist2_plot


#Function 6: Determines differences between two cumulative histograms
#Steps: load two cumulative histograms, loop all bins/arrays to determine differences
#Inputs: two cumulative histograms
#Outputs: height difference for all bins/arrays

def diff_hist(hist1_plot, hist2_plot):
    """Determines differences between two cumulative histograms"""
    bins1 = hist1_plot[0]
    bins2 = hist2_plot[0]
    bins = len(bins1)
    heights = []
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

#Function 7:Function that concatenates the difference histograms

#Function 8: Function that puts it all together and outputs the concatenated
## histograms
#Function 8: Creates and outputs the concatenated histogram
#Steps: wraps all of the functions
#Inputs: image, list of bins, list of blurs
#Outputs: none, shows plot

def Multi_res_hist_full(image, bin_list, gauss_blur_list, show_figs = True):
    """Wraps all functions and produces a plot of height comparisons"""
    arr = np.array(image)
    gauss_blur_images = gauss_filter(image, gauss_blur_list)
    cumulative_Histograms = cumulative_hist(gauss_blur_images, bin_list, show_figs = show_figs)
    plt1=cumulative_Histograms[0]
    plt2=cumulative_Histograms[1]
    heights = diff_hist(plt1, plt2)
    fig2 = plt.figure()
    ax1 = fig2.add_subplot(111)

    ax1.hist(heights, bins=3, density = True, cumulative = True)
    ax1.set_xlabel('Tonal Value')
    ax1.set_ylabel('Frequency')
    ax1.set_xticklabels([]),
    fig2.tight_layout()
    return
