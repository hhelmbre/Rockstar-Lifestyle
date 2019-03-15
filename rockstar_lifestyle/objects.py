#Purpose: To Obtain object stats from the python images

#Import necessary packages
import numpy as np
import rockstar_lifestyle
import scipy
from scipy.ndimage import gaussian_filter
from skimage import filters
from skimage.morphology import watershed
from skimage.feature import peak_local_max
from skimage import measure
from skimage import morphology
from scipy import ndimage
from skimage import segmentation
from skimage import data, feature
import math



#Function 1: Wrapping function that does all following functions in one step
def global_labels(image):
    image_arr = np.array(image)
    thresh = filters.threshold_otsu(image_arr)
    binary = image_arr > thresh
    distance = ndimage.distance_transform_edt(binary)
    local_maxi = peak_local_max(distance, indices=False,
                                footprint=np.ones((3, 3)), labels=binary)
    markers = morphology.label(local_maxi)
    markers[~binary] = -1
    otsu_global_labels = segmentation.random_walker(binary, markers)
    return otsu_global_labels

#Function 2: Performing the Otsu Threshold
def local_labels(image, block_size):
    block_size = block_size
    image_arr = np.array(image)
    adaptive_thresh = filters.threshold_local(image_arr,
                                                block_size, offset=8)
    binary_adaptive = image_arr < adaptive_thresh
    distance = ndimage.distance_transform_edt(binary_adaptive)
    local_maxi = peak_local_max(distance, indices=False,
                            footprint=np.ones((3, 3)), labels=binary_adaptive)
    markers = morphology.label(local_maxi)
    markers[~binary_adaptive] = -1
    local_adaptive_labels = segmentation.random_walker(binary_adaptive, markers)
    return local_adaptive_labels

#Function 3: Creates a binary mask of image
def binary_mask(image):
    pass

#Function 4: Eight item connection of binary binary_mask
def eight_connect():
    pass

#Function 5: Wrapping function for object stats
def obst_basic_wrap():
    pass

#Function 6: Euler number
def euler_number():
    pass

#Function 7: Image centroids
def image_centroids():
    pass

#Function 8: Minimum
def min():
    pass

#Function 9: Max
def max():
    pass

#Function 10: Mean
def mean():
    pass

#Function 11: Median
def median():
    pass

#Function 12: Variance
def variance():
    pass

#Function 13: 10-bin histogram
def tenbin_hist():
    pass
