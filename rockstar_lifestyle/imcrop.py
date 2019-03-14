import json
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image, ImageFilter
import scipy
from scipy.ndimage import gaussian_filter
import skimage
import skimage.io as sio
import tifffile

import warnings

import MultiresHist as mH

#
# Made by: Rockstar-Lifestyle | UW DIRECT | 2019
# 	Team members (alphabetical): Julia Boese, Hawley Helmbrecht, Sage Scheiwiller, David Shackelford
#
# The following py file will involve image cropping and image stack manipulation
#
# Note: Current version only supports png type images for stack creationg; will add
# 		futher functionality later for tif and tif ij images as well
#

class tileData():
	# Createing an identifier for every tile for later use in stacking
	def __init__ (self, res):
		self.im_path = ''
		self.res = res
		self.Data = []

	def extractData(self, path = '', file = '', filetype = '.png'):
		self.im_path = path + file + filetype
		self.Data = sio.imread(self.im_path)

class MRHData():
	# Creating an identifier for every image for later use in neural network
	def __init__(self, imgid, image, MRH, GBL, bin_list):
		self.imgid = imgid
		self.image = image
		self.MRH = MRH
		self.GBL = GBL
		self.bin_list = bin_list

		self.heights = []

	def calc_Heights(self, plt1, plt2):
		self.heights = mH.diff_hist(plt1, plt2)

def stackMRH(stacked_img):
	"""
	The following function acts as a wrapper for the entire py file. It will input an image file
	and given resolution and output a stacked set of cropped tif images. It also saves the set
	into a tif image set on the current folder

	* Current notes: I only have this running for a png input for the purposes of our project, it
	  				 will only output the green band of the images

	Parameters
	----------
	path: str : String of path of file in the form of r"C:/.../.../"
	file: str : String of file name to crop
	filetype: str : Type of file - only use '.png' or '.tif'
	res: int tuple : resolution (res_x, res_y) in pixels of cropped image

	Return
	------
	img_stack : np.uint16 : (n, res_x, res_y) array of n stacks of
							cropped images
	"""

	for k in len(stacked_img[:,_,_]):

		mH.Multi_res_hist_full(stacked_img[k,:,:], bin_list, gauss_blur_list)

def stackLoad(path = '', file = ''):
	"""
	The following function loads the given cropped stacked image into a numpy arrays
	Parameters
	----------
	path: str : String of path of file in the form of r"C:/.../.../"
	file: str : String of file name

	Return
	------
	An (n, res_x, res_y) array of n stacks of cropped images
	"""
	return sio.imread('{}{}.tif'.format(path, file))


def imgCrop(path = '', file = '', filetype = '.png', res = (256,256)):
	"""
	The following function acts as a wrapper for the entire py file. It will input an image file
	and given resolution and output a stacked set of cropped tif images. It also saves the set
	into a tif image set on the current folder

	* Current notes: I only have this running for a png input for the purposes of our project, it
	  				 will only output the green band of the images

	Parameters
	----------
	path: str : String of path of file in the form of r"C:/.../.../"
	file: str : String of file name to crop
	filetype: str : Type of file - only use '.png' or '.tif'
	res: int tuple : resolution (res_x, res_y) in pixels of cropped image

	Return
	------
	img_stack : np.uint16 : (n, res_x, res_y) array of n stacks of
							cropped images
	"""

	def __imgSave(td, stacked_img):
		"""
		The following private function saves the given image array to a tif file with given metadata

		Parameters
		----------
		td: object : tileData() object containing required data

		Return
		------
		stacked_img : np.uint16 : (n, res_x, res_y) array of n stacks of
								  cropped images
		"""
		metadata = json.dumps({"res" : td.res, "orig_Img" : td.file, "dtype" : stacked_img.dtype.str})

		ij = False # For future work with tif ij filetypes
		if ij == True: metadata = {"Info": metadata}
		tifffile.imsave('{}stack_crop_RES{}_{}{}'.format(td.path, td.res, td.file, '.tif'), stacked_img, metadata = metadata, imagej = ij)

	def __crop(td):
		"""
		The following private function crops an image attached to object td
		based on its applied resolution

		Parameters
		----------
		td: object : tileData() object containing required data

		Return
		------
		img_stack : np.uint16 : (n, res_x, res_y) array of n stacks of
								cropped images
		"""

		img_list = []
		_img = td.Data[:,:,1] # Change this to change RGB band (0 == R; 1 == G; 2 == B)
		res_x = td.res[0]
		res_y = td.res[1]

		offset = td.res

		border = ((len(_img[:,0]) % res_x)//2, (len(_img[0,:]) % res_y)//2)

		img_crop = np.zeros(shape = td.res, dtype = 'uint16')
		img_stack = np.zeros(shape = (0, 0, 0, 0), dtype = 'uint16')

		for j in range(len(_img[0,:])//res_x):
		    for i in range(len(_img[:,0])//res_y):
		        # img_loc ='({}:{},{}:{})'.format(i*offset[0]+border[0], i*offset[0]+border[0]+offset[0], j*offset[1]+border[1],j*offset[1]+border[1]+offset[1])
		        img_crop = _img[i*offset[0]+border[0]:i*offset[0]+border[0]+offset[0], j*offset[1]+border[1]:j*offset[1]+border[1]+offset[1]]
		        img_list.append(img_crop)
		img_stack = np.swapaxes(np.dstack(img_list), 2, 0)
		img_stack = np.swapaxes(img_stack, 2, 1)
		return img_stack

	assert len(res) == 2, "Input resolution can only be 2 values"

	if filetype != '.png':
		warnings.warn("The input filetype needs to be a .png for the current version. This will change in future versions")
		filetype = '.png'

	stacked_img = np.zeros(shape = (0, 0, 0, 0), dtype = 'uint16')

	td = tileData(res)
	td.extractData(path, file, filetype)
	stacked_img = __crop(td)
	return stacked_img