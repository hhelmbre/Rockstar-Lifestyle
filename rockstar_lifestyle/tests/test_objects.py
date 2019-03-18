#Purpose: To Obtain object stats from the python images

#Import necessary packages
import numpy as np
import rockstar_lifestyle
import scipy
import objects
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
