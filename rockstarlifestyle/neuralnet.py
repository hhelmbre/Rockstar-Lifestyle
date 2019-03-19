from rockstarlifestyle import multiresolution as mH
from rockstarlifestyle import training_images as tI
from rockstarlifestyle import imcrop as iC
from rockstarlifestyle import objects

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

	# The following is taken from Julia's training_images.py file and
	# modified to fit the given object with no print output. This will
	# all be changed in future iterations, but with time constraints it
	# is left in.
	def rand_im_gen(self, n,
				   res = (256, 256)):
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

	def im_gen_rect(self, n,
				   res = (256, 256)):
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
			warnings.warn("Gaussian blur needs to be performed before " +
						 "Multi Res Histogram")
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

	* Note: If only saving a single object, put in a [list] of len 1 i.e.
	  save_objects([obj], name = 'file_name')

	Parameters
	----------
	dataset : array[objects] :
	name : str : name of

	Baby Dill
	---------
	Whilst walking down the street one day,
	I saw upon the drain,
	A little green dill pickle,
	That was beaten by the rain.

	I picked it up and took it,
	To my house upon the hill.
	I placed it in a tiny bed.
	I named it, Baby Dill.

	I nursed it back to bright green health.
	Its flesh was plump and firm.
	Whenever I would touch it,
	I'm sure I saw it squirm.

	One day when I noticed,
	My babies wrinkly skin.
	I grabbed a jar of pickle juice,
	And I promptly threw it in.

	Within a couple of hours,
	I thought I'd better check.
	My baby dill was missing.
	I was just a wreck.

	That's when I saw my brother,
	He was sitting in his chair.
	Eating my dill pickle.
	As if he didn't care.

	This was the hardest lesson,
	I've ever had to learn.
	Now I can't eat pickles.
	They make my stomach turn.

	- Thomas Plue 2009
	"""

	if ".dat" not in name:
		name = name.rsplit('.', 1)[0] + ".dat"
		warnings.warn("File saved does not end in '.dat', will have problems " +
					 "reading. Automatically renaming to '{}'.".format(name))

	dir_par_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

	if not os.path.exists(dir_par_path + "/data"):
		os.makedirs(dir_par_path + "/data")

	with open(dir_par_path + "/data/" + name, 'wb') as output:
		print("saving to: " + dir_par_path + "/data/")
		for value in dataset:
			pickle.dump(value, output, pickle.HIGHEST_PROTOCOL)


def load_objects(name = 'untitled.dat'):
	"""
	The following function will load an object-based dataset using dill which is a version
	of pickle (a function that stores large amounts of object data) into a subfolder

	Parameters
	----------
	name : str : name of filename to use, default = untitled.dat

	Return
	------
	output : array[objects] : list of objects


	"""
	if ".dat" not in name:
		name = name.rsplit('.', 1)[0] + ".dat"
		warnings.warn("File saved does not end in '.dat', will have problems " +
					 "reading. Automatically renaming to '{}'.".format(name))

	dir_par_path = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

	def _loadall(dir_par_path, name):
		"""
		The following function is a private function for load_objects that will
		load a generator for the file name in the given path

		Parameters
		----------
		dir_par_path : str : folder path of the given file

		Return
		------
		generator : generator : generator of the loaded file
		or
		[] if directory doesn't exist


		"""
		if not os.path.exists(dir_par_path + "/data"):
			warnings.warn("Path doesn't exist. Try downloading" +
						 "something first to create /data/ director.")
			return []

		with open(dir_par_path + "/data/" + name, "rb") as f:
			while True:
				try:
					yield pickle.load(f)
				except EOFError:
					break


	items = _loadall(dir_par_path, name)
	output = []

	for i in items:
		output.append(i)

	return output


def create_train_set(n, prev_set = [],
					 bin_list = [3],
					 gauss_blur_list = [0, 3]):
	"""
	The following function creates a training set of n datasets. If a previous
	set is provided, the function will add to the previous set and output a
	backup set along with the changed set.

	* Note: This function is weak, the image formation is not up to par and will
	  be changed in the future to provide a better training set for the neural
	  network. Right now, the training sets output only protein counts between
	  5600 and 5800 proteins which will not train the neural network properly.

	Parameters
	----------
	n : int : number of training sets to create
	prev_set : list[object] : list of training objects that usr might have
	bin_list : list[int] : list of bins to use in MRH calculations
	gauss_blur_list : list[int] : list of gaussian blur variables to use

	Return
	------
	prev_set : list[objects] : list of training data
	backup : list[objects] : list of backup training data in case new set is
							 unacceptable


	"""
	dataset = []
	lrn_cnt = []
	value = []
	backup = prev_set # In case the user has a good dataset and wants to revert

	for i in range(n):

		learn_data = test_obj((256, 256))
		learn_data.rand_im_gen(1)

		learn_data.calc_GB(gauss_blur_list)
		learn_data.calc_MRH(bin_list, show_figs = False)

		plt1 = learn_data.MRH[0]
		plt2 = learn_data.MRH[1]

		learn_data.calc_heights(plt1,plt2)

		dataset.append(learn_data)
		prev_set.append(learn_data)


	return prev_set, backup

def accuracy(test_x, test_y,
			 classifier,
			 output = False):
	"""
	The following function checks the accuracy of the neural network by
	sending testing data through the classifier and outputing the
	accuracy

	Parameters
	----------
	test_x : np.array : testing data
	test_y : np.array : answered data
	classifier : object : classifier object set by MLPClassifier
	output : bool : Boolean operator to determine whether to output info or not

	Return
	------
	acc : float : accuracy of the neural network


	"""

	df_labels = pd.DataFrame()
	df_labels["success"] = (test_y == classifier.predict(test_x))
	t = 0
	tot = len(df_labels['success'])

	for i in df_labels['success']:
		if i == True:
			t += 1

	if output == True:
		print("Out of {} values, {} were True with an accuracy of {}".format(tot, t, t/tot))

	acc = t/tot

	return df_labels

def neuralnet(dataset = [], NN_settings = None,
			 train = False,
			 save_settings = True,
			 print_acc = False):
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
	dataset : array[object] : dataset to use neural network on
	NN_settings : object : classifier data
	train : bool : decide on whether to train or test
	save_settings : bool : decide on whether to save classifier data to 'data' folder
	print_acc : bool : passes bool to accuracy() to tell function to print accuracy

	Return
	------
	count : list : The counts of the input dataset


	"""

	assert (NN_settings != None or train == True), "Neural Network should be training " \
												   "if there is no settings inputed"

	count = []
	acc = []

	if NN_settings == None:
		classifier = MLPClassifier(solver="lbfgs") # using lbfgs (explained in docstring)
		classifier.hidden_layer_sizes = (100,) # 1 hidden layer with 100 hidden units
		classifier.activation = "tanh" # Using a tanh activation

	else:
		classifier = NN_settings

	if train == True:
		train_X = []
		train_y = []
		value = []
		lrn_dataset = []
		lrn_cnt = []

		for k in range(len(dataset)):
			value.append([])
			for i in range(len(dataset[k].heights)//3):
				value[k].append(dataset[k].heights[i*3])

		for k in range(len(dataset)):
			lrn_dataset.append([])
			lrn_cnt.append(dataset[k].count)
			for ht in value[k]:
				lrn_dataset[k].append(ht[0])

		train_X = lrn_dataset
		train_y = lrn_cnt
		classifier.fit(train_X, train_y)

	if save_settings == True:
		save_objects([classifier], name = 'classifier_info.dat')

	for image in dataset:
		cnt = classifier.predict(image.data)
		count.append(cnt)
		acc.append(accuracy(image.data, cnt, classifier, output = print_acc))

	return count
