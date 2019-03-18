from rockstar_lifestyle import multiresolution as mH
from rockstar_lifestyle import training_images as tI
from rockstar_lifestyle import imcrop as iC
from rockstar_lifestyle import objects

from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC

from skimage import data, feature

import pandas as pd
from PIL import Image, ImageDraw
from random import randint
import numpy as np

import matplotlib.cbook as cbook
import matplotlib.pyplot as plt

import csv
import os
import sys
import warnings

import dill as pickle

#
# Made by: Rockstar-Lifestyle | UW DIRECT | 2019
# 	Team members (alphabetical): Julia Boese, Hawley Helmbrecht, Sage Scheiwiller, David Shackelford
#
# The following py file will involve neural networks and neural network manipulation
#
#

class NN_Settings():

	def __init__(self, learn_rate, classifier):
		self.classifier = classifier
		self.learn_rate = learn_rate

	def change_init(self, learn_rate):
		self.learn_rate = learn_rate
		self.classifier.learning_rate_init = learn_rate

	def print_fitloss(self):
		print(self.learn_rate)
		ax, fig = plt.subplots()
		if self.classifier.solver == "sgd":
			plt.plot(obj.loss_curve_)


class test_obj():
	def __init__(self, res):
		self.res = res
		self.data = []
		self.MRH = []
		self.GB = []
		self.bin_list = []
		self.heights = []
		self.count = 0
	def add_img(self):
		rand_im_gen(1, self.res)
	# The following is taken from Julia's training_images.py file and
	# modified to fit the given object with no print output:
	def rand_im_gen(self, n, res = (256, 256)):
		"""Generates images of random white pixels on black background"""
		#sets up the output array
		imgarray = []
		count = 0
		#loops through images and pixel placement values
		for i in range(n):
			# creates a res pixel image
			img = Image.new('L', res)
			draw = ImageDraw.Draw(img)
			#creates reproducibility
			np.random.seed(123 + i)
			for j in range(0,img.size[0]):
				for k in range(0, img.size[0]):
					a = randint(0,50) + (3 * j)
					b = randint(0,50) + (3 * k)
					c = a + 1
					d = b + 1
					draw.ellipse([a,b,c,d], fill = 255)
					# creates random jumps in the counter
					k = k+randint(90,100)
				j = j+randint(90,100)
			# saves the image as a numpy array
			array = np.array(img)
			# adds new array to the list of arrays
			imgarray.append(array)
		self.data = np.array(img, dtype = float)
		self.count = self.pix_count_array

	def pix_count_im(array, array_index):
		"""Counts the number of colored pixels for a single image"""
		#sets all counters to 0
		black = 0
		obj = 0
		#Creates image from input array
		img = Image.fromarray(array)
		#Loops through the pixels in each image
		for pixel in img.getdata():
			if pixel == 0:
				black += 1
			else:
				obj += 1
		return black, obj
	def pix_count_array(self):

		array = self.data
		i = 0
		pixel_count = pd.DataFrame(columns=['Index','Object',
											'Black', 'Total'])
		#counts through the 'images' in given array
		for i in range(0,len(array)):
			array_index = i
			black, obj = pix_count_im(array, array_index)
			total = obj
			#sums up the pixels counted; should be 62500
			pixel_count.loc[i] = [i, obj, black, total]
		self.count = pixel_count['Object'][0]

	def im_gen_rect(self, n, res = (256, 256)):
		"""Generates images with random rectangles on background"""
		#Seeds the randomness for reproducibilitiy
		np.random.seed(126)
		i=0
		j=2
		k=2
		imgarray = []
		for i in range(0, n):
			#creates a 250x250 pixel image
			img = Image.new('L', res)
			draw = ImageDraw.Draw(img)
			#creates random patterning per image
			y = randint(9,50)
			z = randint(9,50)
			for k in range (2, 240, y):
				for j in range (2, 240, z):
					a = j
					b = k
					c = j + 4
					d = k + 4
					draw.rectangle([a,b,c,d], fill=255)
			#saves the image as a numpy array
			array = np.array(img)
			#adds a callable feature for arrays
			imgarray.append(array)
		self.data = imgarray
	def pix_count_im_rect(array, array_index):
		"""Counts the number of pixels for individual rectangle images"""
		black, obj = pix_count_im(array, array_index)
		#25 pixels per rectangle
		obj_normalized = obj/(25)
		print('object=' + str(obj_normalized) + ', black=' +str(black))
		return black, obj_normalized

	def pix_count_array_rect(self):
		"""Counts the number of rectangles per image"""
		def pix_count_im(array, array_index):
			"""Counts the number of colored pixels for a single image"""
			#sets all counters to 0
			black = 0
			obj = 0
			#Creates image from input array
			img = Image.fromarray(array)
			#Loops through the pixels in each image
			for pixel in img.getdata():
				if pixel == 0:
					black += 1
				else:
					obj += 1
			return black, obj
		def pix_count_im_rect(array, array_index):
			"""Counts the number of pixels for individual rectangle images"""
			black, obj = pix_count_im(array, array_index)
			#25 pixels per rectangle
			obj_normalized = obj/(25)
			print('object=' + str(obj_normalized) + ', black=' +str(black))
			return black, obj_normalized
		array = self.data
		i = 0
		array_index = 1
		#Dataframe for data storage
		pixel_count = pd.DataFrame(columns=['Index','Object',
											'Black','Total'])
		#loops through the images per array
		for i in range(0,len(array)):
			black, obj = pix_count_im_rect(
										   array, array_index)
			array_index = i
			#There are 25 pixels per rectangle
			obj_normalized = obj/(25)
			#62500 pixels should be counted for each 250x250 image
			total = black + obj
			pixel_count.loc[i] = [i, obj_normalized, black, total]
		self.count = pixel_count

	def calc_MRH(self, bins,
				 show_figs = False):
		cumulative_data = []
		if self.GB == []:
			warnings.warn("Gaussian blur needs to be performed before Multi Res Histogram")
		self.MRH = mH.cumulative_hist(self.GB, bins, show_figs = show_figs)
		for i in range(len(self.MRH[0][:])):
			self.bin_list.append(self.MRH[i][1])

	def calc_GB(self, gauss_blur_list):
		self.GB = mH.gauss_filter(self.data, gauss_blur_list)

	def calc_heights(self, plt1,
					 plt2):
		self.heights = mH.diff_hist(plt1, plt2)



def save_objects(dataset, name = 'untitled.dat'):
	"""
	The following function will save an object set using dill which is a version
	of pickle (a function that stores large amounts of object data) into a subfolder
	named 'data'. The

	Parameters
	----------
	dataset : array[objects] :
	name : str : name of

	"""
	if ".dat" not in name:
		name = name.rsplit('.', 1)[0] + ".dat"
		warnings.warn("File saved does not end in '.dat', will have problems reading. Automatically renaming to '{}'.".format(name))

	dir_par_path = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0]

	with open(dir_par_path + 'data/' + name, 'wb') as output:

		for value in dataset:
			pickle.dump(value, output, pickle.HIGHEST_PROTOCOL)


def load_objects(name = 'untitled.dat'):
	"""
	The following function will load a object-based dataset

	Parameters
	----------
	name : str : name of filename to use, default = untitled.dat


	Return
	------
	output : array[objects] : list of objects
	"""


	file = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0] + 'data/'
	def _loadall():
		with open(file + name, "rb") as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break
	items = _loadall()
	output = []
	for i in items:
		output.append(i)
	return output


def create_neural_set(stacked_img, prev_set = None,
					   bin_list = [3], gauss_blur_list = [0, 3]):
	"""
	The following function creates a test set based on stacked object array


	Parameters
	----------
	 :  :

	Return
	------
	 :  :
	"""
	if prev_set == None:
		obj_list = []
	else:
		obj_list = prev_set
	obj_list.append(object)
	return obj_list

def accuracy(test_x, test_y,
			 classifier, output = False):
	"""
	The following function checks the accuracy of the neural network by
	sending testing data through the classifier and outputing the
	accuracy

	Parameters
	----------
	test_x : np.array :
	test_y : np.array :
	classifier : object : classifier object set by MLPClassifier
	output : Bool : Boolean operator to determine whether to output info or not

	Return
	------
	acc : float : accuracy of the neural network
	"""
	df_labels = pd.DataFrame()
	df_labels["success"] = (train_y == classifier.predict(train_X))
	t = 0
	tot = len(df_labels['success'])
	for i in df_labels['success']:
		if i == True:
			t += 1
	if output == True:
		print("Out of {} values, {} were True with an accuracy of {}".format(tot, t, t/tot))
	acc = t/tot
	return acc

def neuralnet(obj = []):
	"""
	The following function is a wrapper function that will use a neural network in
	order to best estimate the protein count of the input images. The solver used
	in this neural network is L-BFGS which is a quasi-Newton method that is
	theoretically and experimentally verified to have a faster convergence and works
	well with low-dimensional input. L-BFGS does not work well in other settings
	because of its high memory requirement and lack of use of minibatches. There are
	other methods that can be tried (Adam, SGD BatchNorm , Adadelta, Adagrad), but
	L-BFGS was the best choice for this application and for the time constraint given
	in producing this package.

	Parameters
	----------
	obj : array[object] : dataset to use neural network on


	Return
	------
	 :  :
	"""

	count = []

	train_y = lrn_cnt
	train_X = lrn_dataset

	classifier = MLPClassifier(solver="lbfgs")
	classifier.hidden_layer_sizes = (100,) # 1 hidden layer with 100 hidden units
	classifier.activation = "tanh" # Using a tanh activation
	classifier.fit(train_X, train_y)

	for image in obj:
		count.append(classifier.predict(image.data))
	return count