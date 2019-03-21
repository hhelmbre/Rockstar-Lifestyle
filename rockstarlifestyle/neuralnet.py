# pylint: disable=W0312
# Ignoring indentation/spacing mixup. I didn't know tabs are bad

# Made by: Rockstar-Lifestyle | UW DIRECT | 2019
# Team members (alphabetical): Julia Boese, Hawley Helmbrecht,
# 								 Sage Scheiwiller, David Shackelford
#
# The following py file will involve neural networks and neural
# network manipulation including saving and loading object stats
#
# Things to improve on in the future:
# 	* Better training data; more optimized for use in NN. This is the
# 	most important b/c the object creation was made separately from the
# 	NN code so I had to just c/p a lot as class functions to make it
# 	work and it's all very sloppy and I'm not happy with it at all.
# 	* Better class organization; need to merge with classes from the
# 	imcrop file. I think the ID class from imcrop can be modified to do
# 	a lot of the things in this file. Maybe make a .py dedicated to
# 	object creation/methods? I'm a little embarrased about the
# 	organization now to be honest...
# 	* Pickling can be handled better; maybe find a different solution?
# 	Pickling can be a little dangerous to use since people can create
# 	Malicious pickles (aka pickle bombs).
# 	see: https://intoli.com/blog/dangerous-pickles/
# 	This was just a quick solution for me at the moment
# 	so that I could have persistant NN data. I would like a better
# 	solution. Additionally, the pickle file is so large now, it's hard
# 	to deal with. I need to install and use Git Large File Storage to
# 	store the file on github which is a little bit of a bother for
# 	me and anyone who wants to use the repo.
# 	* NN has fairly good useability, but can get confusing. I tried
# 	to give the NN plenty of options. The user can either train or test
# 	using the same function, but I would like to alter it a little bit.
# 	This file will hopefully be used by Nance lab in the future and not
# 	everyone in that lab is a coder so I would love to make it as easy
# 	to use and intuitive as possible.
# 	* Just get a better NN in general, I had a hard time w/ this stuff.
# 	I researched it like crazy and due to time constraints, I stuck
# 	with the NN I have now. I would not only like to look more into
# 	adjustments (methods other than lbfgs, different hidden layer sizes,
# 	different activations), but I would also like to look into
# 	additions to the NN. I particuarly liked reading these papers:
# 	"Learning to Count Objects in Images" (2010) Lempitsky, V. et al
#	"Interactive Object Counting" (2014) Arteta C. et al
#	but there is a lot more out there about counting using NNs that
#	I've been looking into.

import os
import warnings

from random import randint

from sklearn.neural_network import MLPClassifier

import pandas as pd
from PIL import Image, ImageDraw

import numpy as np

import matplotlib.pyplot as plt

import dill as pickle

from rockstarlifestyle import multiresolution as mH



class NNSettings():
	"""
	Stores settings for neural network, mostly used for sgd
	"""
	def __init__(self, learn_rate, classifier):
		self.classifier = classifier
		self.learn_rate = learn_rate

	def change_init(self, learn_rate):
		"""
		Changes initial value for sgd
		"""
		self.learn_rate = learn_rate
		self.classifier.learning_rate_init = learn_rate

	def print_fitloss(self):
		"""
		Prints the fit loss function if the solver is sgd
		"""
		print(self.learn_rate)
		_, _ = plt.subplots()
		if self.classifier.solver == "sgd":
			plt.plot(self.classifier.loss_curve_)


class TestObj():
	"""
	Object for test and training values
	"""
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
	def rand_im_gen(self, n, res=(256, 256)):
		#Generates images of random white pixels on black background
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
			for j in range(0, img.size[0]):
				for k in range(0, img.size[0]):
					a = randint(0, 50) + (3 * j)
					b = randint(0, 50) + (3 * k)
					c = a + 1
					d = b + 1
					draw.ellipse([a, b, c, d], fill=255)
					# creates random jumps in the counter
					k = k + randint(90, 100)
				j = j + randint(90, 100)
			# saves the image as a numpy array
			array = np.array(img)
			# adds new array to the list of arrays
			imgarray.append(array)
		self.data = np.array(img, dtype=float)
		self.count = self.pix_count_array

	def _pix_count_im(self, array, array_index):
		"""
		Counts the number of colored pixels for a single image
		"""
		# sets all counters to 0
		black = 0
		obj = 0
		# Creates image from input array
		img = Image.fromarray(array)
		# Loops through the pixels in each image
		for pixel in img.getdata():
			if pixel == 0:
				black += 1
			else:
				obj += 1
		return black, obj

	def pix_count_array(self):
		"""
		Counts number of pixels in array
		"""
		array = self.data
		i = 0
		pixel_count = pd.DataFrame(columns=['Index', 'Object',
                                            'Black', 'Total'])
		# counts through the 'images' in given array
		for i in range(0, len(array)):
			array_index = i
			black, obj = self._pix_count_im(array, array_index)
			total = obj
			#sums up the pixels counted; should be 62500
			pixel_count.loc[i] = [i, obj, black, total]
		self.count = pixel_count['Object'][0]

	def im_gen_rect(self, n, res=(256, 256)):
		# Generates images with random rectangles on background
		# Seeds the randomness for reproducibilitiy
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
			y = randint(9, 50)
			z = randint(9, 50)
			for k in range(2, 240, y):
				for j in range(2, 240, z):
					a = j
					b = k
					c = j + 4
					d = k + 4
					draw.rectangle([a, b, c, d], fill=255)

			# saves the image as a numpy array
			array = np.array(img)
			# adds a callable feature for arrays
			imgarray.append(array)
		self.data = imgarray
	def pix_count_im_rect(self, array, array_index):
		"""
		Counts the number of pixels for individual rectangle images
		"""
		def _pix_count_im(array, array_index):
			"""
			Counts the number of colored pixels for a single image
			"""
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

		black, obj = _pix_count_im(array, array_index)
		# 25 pixels per rectangle
		obj_normalized = obj/(25)
		print('object=' + str(obj_normalized) + ', black=' +str(black))
		return black, obj_normalized


	def pix_count_array_rect(self):
		"""
		Counts the number of rectangles per image
		"""
		def _pix_count_im(array, array_index):
			#Counts the number of colored pixels for a single image
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
		def _pix_count_im_rect(array, array_index):
			"""
			Counts the number of pixels of indiv rectangle images
			"""
			black, obj = _pix_count_im(array, array_index)
			# 25 pixels per rectangle
			obj_normalized = obj/(25)
			print('object=' +
			      str(obj_normalized) +
			      ', black=' +
			      str(black))
			return black, obj_normalized

		array = self.data
		i = 0
		array_index = 1
		#Dataframe for data storage
		pixel_count = pd.DataFrame(columns=['Index', 'Object',
                                            'Black', 'Total'])
		#loops through the images per array
		for i in range(0, len(array)):
			black, obj = _pix_count_im_rect(array, array_index)
			array_index = i
			#There are 25 pixels per rectangle
			obj_normalized = obj/(25)
			#62500 pixels should be counted for each 250x250 image
			total = black + obj
			pixel_count.loc[i] = [i, obj_normalized, black, total]
		self.count = pixel_count

	def calc_MRH(self, bins, show_figs=False):
		"""
		Calculates MRH data
		"""
		if self.GB == []:
			warnings.warn("Gaussian blur needs to be performed "\
						 "before Multi Res Histogram")
		self.MRH = mH.cumulative_hist(self.GB, bins,
									  show_figs=show_figs)
		for i in range(len(self.MRH[0][:])):
			self.bin_list.append(self.MRH[i][1])

	def calc_GB(self, gauss_blur_list):
		"""
		Calculates Gaussian Blur
		"""
		self.GB = mH.gauss_filter(self.data, gauss_blur_list)

	def calc_heights(self, plt1, plt2):
		"""
		Returns heights of histogram given plt1 and plt2
		"""
		self.heights = mH.diff_hist(plt1, plt2)


def save_objects(dataset, name='untitled.dat'):
	"""
	The following function will save an object set using dill which is
	a version of pickle (a function that stores large amounts of
	object data) into a subfolder named 'data'.

	* Note: If only saving a single object, put in a [list] of len 1
	  i.e. save_objects([obj], name = 'file_name')

	Parameters
	----------
	dataset : array[objects] : array of objects to save
	name : str : name of file pickle will be saved to

	Return
	------
	One big 'ol thicc pickle

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
	(sorry)
	"""

	if ".dat" not in name:
		name = name.rsplit('.', 1)[0] + ".dat"
		warnings.warn("File saved does not end in '.dat', will "\
					 "have problems reading. Automatically "\
					 "renaming to '{}'.".format(name))

	dir_par_path = os.path.dirname(
	    os.path.realpath(__file__)).replace('\\', '/')

	if not os.path.exists(dir_par_path + "/data"):
		os.makedirs(dir_par_path + "/data")

	with open(dir_par_path + "/data/" + name, 'wb') as output:
		print("saving to: " + dir_par_path + "/data/")
		for value in dataset:
			pickle.dump(value, output, pickle.HIGHEST_PROTOCOL)


def load_objects(name='untitled.dat'):
	"""
	The following function will load an object-based dataset using dill
	which is a version of pickle (a function that stores large amounts
	of object data) into a subfolder

	Parameters
	----------
	name : str : name of filename to use, default = untitled.dat

	Return
	------
	output : array[objects] : list of objects


	"""
	if ".dat" not in name:
		name = name.rsplit('.', 1)[0] + ".dat"
		warnings.warn("File saved does not end in '.dat', will "\
					 "have problems reading. Automatically "\
					 "renaming to '{}'.".format(name))

	dir_par_path = os.path.dirname(
	    os.path.realpath(__file__)).replace('\\', '/')

	def _loadall(dir_par_path, name):
		"""
		The following function is a private function for load_objects
		that will load a generator for the file name in the given path

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

		with open(dir_par_path + "/data/" + name, "rb") as file:
			while True:
				try:
					yield pickle.load(file)
				except EOFError:
					break


	items = _loadall(dir_par_path, name)
	output = []

	for i in items:
		output.append(i)

	return output


def create_train_set(numb_sets=None,
                     prev_set=None,
                     bin_list=None,
                     gauss_blur_list=None):
	"""
	The following function creates a training set of n datasets. If a
	previous set is provided, the function will add to the previous set
	and output a backup set along with the changed set.

	* Note: This function is weak, the image formation is not up to par
	  and will be changed in the future to provide a better training
	  set for the neural network. Right now, the training sets output
	  only protein counts between 5600 and 5800 proteins which will not
	  train the neural network properly.

	Parameters
	----------
	numb_sets : int : number of training sets to create
	prev_set : list[object] : list of training objs that usr might have
	bin_list : list[int] : list of bins to use in MRH calculations
	gauss_blur_list : list[int] : list of gauss blur vars to use

	Return
	------
	prev_set : list[objects] : list of training data
	backup : list[objects] : list of backup training data in case new
							 set is unacceptable


	"""

	if prev_set is None:
		prev_set = []
	if numb_sets is None:
		numb_sets = 0
	if bin_list is None:
		bin_list = [3]
	if gauss_blur_list is None:
		gauss_blur_list = [0, 3]
	dataset = None
	dataset = []
	backup = prev_set # In case the user wants to revert

	for _ in range(numb_sets):

		learn_data = TestObj((256, 256))
		learn_data.rand_im_gen(1)

		learn_data.calc_GB(gauss_blur_list)
		learn_data.calc_MRH(bin_list, show_figs=False)

		plt1 = learn_data.MRH[0]
		plt2 = learn_data.MRH[1]

		learn_data.calc_heights(plt1, plt2)

		dataset.append(learn_data)
		prev_set.append(learn_data)


	return prev_set, backup

def accuracy(test_x,
             test_y,
             classifier,
             output=False):
	"""
	The following function checks the accuracy of the neural network by
	sending testing data through the classifier and outputing the
	accuracy

	Parameters
	----------
	test_x : np.array : testing data
	test_y : np.array : answered data
	classifier : object : classifier object set by MLPClassifier
	output : bool : Boolean operator to determine whether to output
					info or not

	Return
	------
	acc : float : accuracy of the neural network


	"""

	df_labels = pd.DataFrame()
	df_labels["success"] = (test_y == classifier.predict(test_x))
	tru = 0
	tot = len(df_labels['success'])

	for i in df_labels['success']:
		if i:
			tru += 1

	if output:
		print("Out of {} values, {} were True with an accuracy" \
			 " of {}".format(tot, tru, tru/tot))


	return df_labels

def neuralnet(dataset=None,
              nn_settings=None,
              train=False,
              save_settings=True,
              print_acc=False):
	"""
	The following function is a wrapper function that will use a neural
	network in order to best estimate the protein count of the input
	images. The solver used in this neural network is L-BFGS which is a
	quasi-Newton method that is theoretically and experimentally
	verified to have a faster convergence and works well with low-
	dimensional input. L-BFGS does not work well in other settings
	because of its high memory requirement and lack of use of
	minibatches. There are other methods that can be tried (Adam, SGD
	BatchNorm , Adadelta, Adagrad), but L-BFGS was the best choice for
	this application and for the time constraint given in producing
	this package.

	Parameters
	----------
	dataset : array[object] : dataset to use neural network on
	nn_settings : object : classifier data
	train : bool : decide on whether to train or test
	save_settings : bool : decide on whether to save classifier data
						   to 'data' folder
	print_acc : bool : passes bool to accuracy() to tell function to
					   print accuracy

	Return
	------
	count : list : The counts of the input dataset


	"""
	if dataset is None:
		dataset = []
	count = None
	acc = None
	train_x = None
	train_y = None
	value = None
	lrn_dataset = None
	lrn_cnt = None

	assert (nn_settings is not None
		or train), "Neural Network should be training " \
                   "if there is no settings inputed"

	count = []
	acc = []

	if nn_settings is None:
		# using lbfgs (explained in docstring)
		classifier = MLPClassifier(solver="lbfgs")
		# 1 hidden layer with 100 hidden units
		classifier.hidden_layer_sizes = (100,)
		# Using a tanh activation
		classifier.activation = "tanh"

	else:
		classifier = nn_settings

	if train:
		train_x = []
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
			for ht_val in value[k]:
				lrn_dataset[k].append(ht_val[0])
		train_x = lrn_dataset
		train_y = lrn_cnt
		classifier.fit(train_x, train_y)

	if save_settings:
		save_objects([classifier], name='classifier_info.dat')

	for image in dataset:
		cnt = classifier.predict(image.data)
		count.append(cnt)
		acc.append(accuracy(image.data, cnt,
			            classifier,
			            output=print_acc))

	return count
