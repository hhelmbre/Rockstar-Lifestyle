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

#Function X: Obtaining the Global Threshold binary
def global_binary(image):
    '''obtains the binary using the Global Otsu Threshold'''
    image_arr = np.array(image)
    thresh = filters.threshold_otsu(image_arr)
    global_binary = image_arr > thresh
    return global_binary

def local_binary(image, block_size):
    '''obtains th ebinary of the image using a local adaptive threshold'''
    image_arr = np.array(image)
    adaptive_thresh = filters.threshold_local(image_arr,
                                                    block_size, offset=8)
    binary_adaptive = image_arr < adaptive_thresh
    return binary_adaptive

#Function X: Obtaining the Local Adaptive Threshold Binary

#Function X: Wrapping function that does all following functions in one step
def global_labels(image):
    '''obtains the labels for objects using the global otsu threshold'''
    binary = global_binary(image)
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
    binary = local_binary(image, block_size)
    distance = ndimage.distance_transform_edt(binary)
    local_maxi = peak_local_max(distance, indices=False,
                            footprint=np.ones((3, 3)), labels=binary)
    markers = morphology.label(local_maxi)
    markers[~binary] = -1
    local_adaptive_labels = segmentation.random_walker(binary, markers)
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

#Function x: finds the distance between an object and image centroid
def centroid_distance(image_centroid, object_centroid, row):
    '''computes distance between an object centroid and image centroid'''
    X1 = image_centroid[0]
    Y1 = image_centroid[1]
    X2 = object_centroid[row][0]
    Y2 = object_centroid[row][1]
    distance = math.sqrt((X1-X2)**2+(Y1-Y2)**2)
    return distance

def distancesarr(image_centroid, object_centroids):
    distances = []
    j = 0
    for row in object_centroids:
        distance = centroid_distance(image_centroid, object_centroids, j)
        distances.append(distance)
        j +=1
    return distances

def objectcentroids(image, block_size):
    '''obtaining the object centroids'''
    global_binarys = global_binary(image)
    object_centroids = feature.blob_log(global_binarys)
    local_binarys = local_binary(image, block_size)
    object_centroids_local = feature.blob_log(local_binarys)
    return object_centroids, object_centroids_local

def distance_histograms(image, block_size):
    '''obtaining 10-bin histograms of centroid distances'''
    otsu_global_labels = global_labels(image)
    local_adaptive_labels = local_labels(image, block_size)

    properties_global = measure.regionprops(otsu_global_labels)
    properties_local = measure.regionprops(local_adaptive_labels)

    image_centroid = properties_global[0].centroid
    image_centroid_adaptive = properties_local[0].centroid

    object_centroids, object_centroids_local = objectcentroids(image, block_size)

    distances_global = distancesarr(image_centroid, object_centroids)
    distances_local = distancesarr(image_centroid_adaptive, object_centroids_local)

    fig = plt.figure()
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    ax1.hist(distances_global, bins=10, density = True, cumulative = False)
    ax1.set_title('Global Otsu Threshold')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Pixel Distance')

    ax2.hist(distances_local, bins=10, density = True, cumulative = False)
    ax2.set_title('Local Threshold')
    ax2.set_ylabel('Frequency')
    ax2.set_xlabel('Pixel Distance')

    fig.tight_layout()
    return

def objectnumber(image, block_size):
    global_binarys = global_binary(image)
    object_centroids = feature.blob_log(global_binarys)

    local_binarys = local_binary(image, block_size)
    object_centroids_local = feature.blob_log(local_binarys)

    object_number_global = len(object_centroids)
    print('Gobal Threshold Object Number:     ', object_number_global)

    object_number_local = len(object_centroids_local)
    print('Local Threshold Object Number:    ', object_number_local)
    return
