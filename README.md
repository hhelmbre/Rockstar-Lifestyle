<p>
	<img src="https://github.com/hhelmbre/Rockstar-Lifestyle/blob/master/doc/Logo.png" width="10%" align="left">
</p>

# Rockstar-Lifestyle
## Protein Characteriziation Package
This package can be used to take fluorescence microscopy images of cell 
staining, run the data through a fast-fourier transform to obtain 
localization information, apply the localization information data to a 
multi-resolution histogram which provides patterning information from the 
image.  These patterns obtained can then be characterized based on the 
neural network, trained through images generated as part of this package.  
The pakcage can be extended to use with various other types of protein 
visualization images although the initial intent was to use it with 
whole-cell staining. Referring to the poster in the doc directory will 
provide a more specific overview of the project. 

### How to Install

1. Use `git clone` to clone repository
2. Use ` pip install .` to install and run functions
  
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
		test_multiresolution.py
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
	P14_healthy_40x_hippo_scan_MaxIP.png
	P35_LPS_ipsi_40x_hippo_scan_MaxIP.png
**examples/**
	HowTo--edges.py.ipynb
	Functionalized-Multires-histograms.ipynb
	Object-Statistics.ipynb
	Training_Images_Examples.ipynb
	first-four-moments.ipynb
	fourier_transform-with-multires-hist.ipynb
	imcrop_demo.ipynb
**doc/**
	componentsketch.pdf
	poster.pdf
	tech_review.pdf
	use_cases.MD
	Logo.png
.gitignore
License.txt
README.md
Rockstar-Lifestyle-Logo.png
requirements.txt
setup.py
```

## Usage



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
for providing the testing images.  
