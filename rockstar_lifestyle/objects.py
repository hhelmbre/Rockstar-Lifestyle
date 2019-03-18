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
import matplotlib.pyplot as plt



#Function 1: Wrapping function that does all following functions in one step
def global_labels(image):
    '''obtains the labels for objects using the global otsu threshold'''
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
    '''obtains the lables using a local adaptive threshold for objects'''
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
def object_area_hist(properties_local, properties_global):
    areas_local_adaptive = [prop.bbox_area for prop in properties_local]
    areas_global = [prop.bbox_area for prop in properties_global]
    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    ax1.hist(areas_global, bins=10, density = True, cumulative = False)
    ax1.set_title('Global Otsu Threshold')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Object Area')

    ax2.hist(areas_local_adaptive, bins=10, density = True, cumulative = False)
    ax2.set_title('Local Threshold')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Object Area')

    fig.tight_layout()
    return
