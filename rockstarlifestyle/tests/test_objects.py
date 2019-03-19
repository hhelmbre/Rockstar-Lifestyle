#Purpose: To Obtain object stats from the python images

#Import necessary packages
from rockstarlifestyle import objects, preprocessing
import numpy as np
import scipy
from skimage.feature import peak_local_max
from skimage import measure, morphology, segmentation, data, feature, filters
from scipy import ndimage
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance


# def test_global_binary():
#     """Test: obtains the binary using the Global Otsu Threshold """
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     #running the functions
#     global_binary = objects.global_binary(image)
#     #asserts and checks
#     return
#
# def test_local_binary():
#     """Test: obtains the binary of the image using a local adaptive threshold"""
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     #running the functions
#     binary_adaptive = objects.local_binary(image, block_size)
#     #asserts and checks
#     return
#
# def test_global_labels():
#     """Test: obtains the labels for objects using the global otsu threshold"""
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     image = preprocessing.image_contrast(split, 2)
#     #running the functions
#     otsu_global_labels = objects.global_labels(image)
#     #asserts and checks
#     return
#
# def test_local_labels():
#     """Test: obtains the lables using a local adaptive threshold for objects"""
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     #running the functions
#     local_adaptive_labels = objects.local_labels(image, block_size)
#     #asserts and checks
#     return
#
# def test_object_area_hist():
#     """Test: makes 10-bin histograms of the object areas"""
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     local_adaptive_labels = objects.local_labels(image, block_size)
#     otsu_global_labels = objects.global_labels(image)
#     #final inputs
#     properties_local = measure.regionprops(local_adaptive_labels)
#     properties_global = measure.regionprops(otsu_global_labels)
#     #running the functions
#     objects.object_area_hist(properties_local, properties_global)
#     #asserts and checks
#     return
# #
#
# def test_centroid_distance():
#     """Test: computes distance between an object centroid and image centroid"""
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     otsu_global_labels = objects.global_labels(image)
#     properties_global = measure.regionprops(otsu_global_labels)
#     image_centroid = properties_global[0].centroid
#     #running the functions
#     distance = objects.centroid_distance(image_centroid, object_centroid, row)
#     #asserts and checks
#     return

def test_distancesarr():
    """Test: gets the distances between image and objects"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(image, desired_color)
    image = preprocessing.image_contrast(split, 2)
    block_size = 15
    #final inputs
    otsu_global_labels = objects.global_labels(image)
    properties_global = measure.regionprops(otsu_global_labels)
    image_centroid = properties_global[0].centroid
    global_binarys = objects.global_binary(image)
    object_centroids = feature.blob_log(global_binarys)
    row = 3
    #running the functions
    distances = objects.distancesarr(image_centroid, object_centroids)
    #asserts and checks
    return

# def test_objectcentroids():
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     contrast_image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     #running the functions
#     object_centroids, object_centroids_local = objects.objectcentroids(contrast_image, block_size)
#     #asserts and checks
#     return
#
# def test_distance_histograms():
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     contrast_image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     #running the functions
#     objects.distance_histograms(contrast_image, block_size)
#     #asserts and checks
#     return
#
# def test_objectnumber():
#     #inputs for functions
#     image = Image.open('../data/protein_matrix_image.png')
#     desired_color = 'b'
#     #processing
#     split = preprocessing.color_split_image(image, desired_color)
#     contrast_image = preprocessing.image_contrast(split, 2)
#     block_size = 15
#     #running the functions
#     objects.objectnumber(contrast_image, block_size)
#     #asserts and checks
#     return

def test_stats():
    """Test: gets basic stats for whatever property input"""
    #inputs for functions
    image = Image.open('../data/protein_matrix_image.png')
    desired_color = 'b'
    #processing
    split = preprocessing.color_split_image(image, desired_color)
    image = preprocessing.image_contrast(split, 2)#inputs for functions
    #labels
    otsu_global_labels = objects.global_labels(image)
    properties_global = measure.regionprops(otsu_global_labels)
    image_centroid = properties_global[0].centroid
    global_binarys = objects.global_binary(image)
    object_centroids = feature.blob_log(global_binarys)
    row = 3
    distance = objects.centroid_distance(image_centroid, object_centroids, row)    #running the functions
    #final inputs
    property = distance
    #running the functions
    objects.stats(property)
    #asserts and checks
    return
