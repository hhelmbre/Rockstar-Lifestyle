#Purpose: To Obtain object stats from the python images

#Import necessary packages
import numpy as np
import rockstar_lifestyle
import scipy
from rockstarlifestyle import objects, preprocessing

from PIL import Image, ImageFilter, ImageEnhance
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


def test_global_binary():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    #running the functions
    global_binary = objects.global_binary(image)
    #asserts and checks
    return

def test_local_binary():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #running the functions
    binary_adaptive = objects.local_binary(image, block_size)
    #asserts and checks
    return

def test_global_labels():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    image = preprocessing.image_contrast(split, 2)
    #running the functions
    otsu_global_labels = objects.global_labels(image)
    #asserts and checks
    return

def test_local_labels():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #running the functions
    local_adaptive_labels = objects.local_labels(image, block_size)
    #asserts and checks
    return

def test_object_area_hist():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    image = preprocessing.image_contrast(split, 2)
    block_size = 15
    local_adaptive_labels = objects.local_labels(image, block_size)
    otsu_global_labels = objects.global_labels(image)
    #final inputs
    properties_local = measure.regionprops(local_adaptive_labels)
    properties_global = measure.regionprops(otsu_global_labels)
    #running the functions
    objects.object_area_hist(properties_local, properties_global)
    #asserts and checks
    return


def test_centroid_distance():
    #inputs for functions
    #running the functions
    otsu_global_labels = global_labels(image)
    properties_global = measure.regionprops(otsu_global_labels)
    image_centroid = properties_global[0].centroid
    distance = objects.centroid_distance(image_centroid, object_centroid, row)
    #asserts and checks
    return

def test_distancesarr():
    #inputs for functions
    #running the functions
    #asserts and checks
    return

def test_objectcentroids():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    contrast_image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #running the functions
    object_centroids, object_centroids_local = objects.objectcentroids(contrast_image, block_size)
    #asserts and checks
    return

def test_distance_histograms():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    contrast_image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #running the functions
    objects.distance_histograms(contrast_image, block_size)
    #asserts and checks
    return

def test_objectnumber():
    #inputs for functions
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(Image, desired_color)
    contrast_image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #running the functions
    objects.objectnumber(contrast_image, block_size)
    #asserts and checks
    return

def test_stats():
    #inputs for functions
    #running the functions
    #asserts and checks
    return
