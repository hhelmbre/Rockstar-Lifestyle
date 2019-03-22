<p>
	<img src="https://github.com/hhelmbre/Rockstar-Lifestyle/blob/master/doc/Logo.png" width="10%" align="left">
</p>

# Rockstar-Lifestyle
## Protein Characteriziation Package
This package can be used to take fluorescence microscopy images of cell 
staining, run the data through a fast-fourier transform to obtain 
localization information, tested for edge and object statistics, and then 
the localization data and edge and object stats can be applied to a 
multi-resolution histogram which provides patterning information from the 
image. These patterns, edge stats, and object stats obtained can then be 
characterized based on the neural network, that was trained trained through
a set of images generated as part of this package and in the future of this
package also trained through a data set of well-characterized images from 
published studies. The package can be extended to use with various other 
types of protein visualization images although the initial intent was to 
use it with whole-cell staining of neural images. Referring to the poster 
in the doc directory will provide a more specific overview of the project. 

### How to Install

1. Use `git clone` to clone repository into your desired directory
2. Use ` pip install .` to install the package from the `setup.py` file
3. Run functions
  
### Software Dependencies
- Python3
- For python packages see requirements.txt


## Organization of the project
```
**rockstarlifestyle/**
	**data/**
		classifier_info.dat
		protein_matrix_image.png
		stacked_img_test.dat
		training_set.dat
	**tests/**
		_init_.py
		test_edges.py
		test_fouriertransform.py
		test_imcrop.py
		test_multiresolution.py
		test_neuralnet.py
		test_objects.py
		test_preprocessing.py
		test_training_images.py
	_init_.py
	edges.py
	fouriertransform.py
	imcrop.py
	multiresolution.py
	neuralnet.py
	objects.py
	preprocessing.py
	training_images.py
**Images/**
	P10_LPS_ipsi_40x_hippo_scan_MaxIP.png
	P10_PAM_ipsi_40x_hippo_scan_MaxIP.png
	P14_healthy_40x_hippo_scan_MaxIP.png
	P35_LPS_ipsi_40x_hippo_scan_MaxIP.png
	gjerstorff_et_al.png
	ma_et_al.jpg
	salsman_et_al.png
	shu_et_al.png
**examples/**
	HowTo--edges.py.ipynb
	Functionalized-Multires-histograms.ipynb
	Object-Statistics.ipynb
	Training_Images_Examples.ipynb
	fourier_transform-with-multires-hist.ipynb
	imcrop_demo.ipynb
	neural_network_demo.ipynb
**doc/**
	componentsketch.pdf
	poster.pdf
	tech_review.pdf
	use_cases.MD
	Logo.png
.gitignore
License.txt
README.md
requirements.txt
setup.py
```

## Usage

To use this package it is best to begin with the functions in the 
`preprocessing.py` file to enhance the contrast of the images and splits
the colors. Then using the `imcrop.py` functions one can crop images into 
equal 250x250 resolution images that can eventually be run through the neural
network functions of `neuralnet.py`.  Images can also be run through the
functions in `fouriertransform.py` and `multiresolution.py` to obtain the
fourier transform of each image as well as the multi-resolution histogram
for each image.  Additionally, the images can be used with the functions in 
`objects.py` and `edges.py` to obtain object and edge statistics. For 
training the neural network one can use the `training_images.py` file to
generate images for training purposes.  For other ways to train the neural
one can use any images they desire and run them through the functions as 
documented above. Examples of usage for each `.py` file is provided in the 
`examples` directory.

## Contributing

Pull requests accepted through hhelmbre/Rockstar-Lifestyle

## Authors

Julia Boese - jnboese  
Hawley Helmbrecht - hhelmbre  
Sage Scheiwiller - SageScheiwiller  
David Shackelford - dash2927  

## License
```
MIT Licence Copyright (c) 2019 hhelmbre
```
## Acknowledgements
We would like to thank Professor David Beck and the fantastic group of 
teaching assistants in the DIRECT program, especially Chad Curtis, for all 
of their help and guidance with the development of this project.

We would also like to thank the Nance Lab and the University of Washington 
for providing the testing images. Continuing, the training images within
the `Images` directory were obtained from the groups they are named after. 
The journal ids are as follows, pbio.1001041, ASN.2013091017, ppat.1000100, 
and PMC2361341.
