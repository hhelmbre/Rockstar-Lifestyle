<p>
	<img src="https://raw.githubusercontent.com/hhelmbre/Rockstar-Lifestyle/master/Logo.png" width="10%" align="left">
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
whole-cell staining. Referring to the ....... poster will provide a more 
specific overview of the project. 

### How to Install

1. Use `git clone` to clone repository
2. Use ` pip install .` to install and run functions
  
### Software Dependencies
- Python3
- For python packages see requirements.txt


## Organization of the project
```
**RockstarLifestyle/**
	**tests/**
		Test_Photo_fromMike.png
		_init.py
		test_Filter_Functions.py
		test_fouriertransform.py
		test_image_training_shapes.py
		test_multiresHist.py
		test_preprocessing.py
	Filter_Functions.py
	Image_training_circles.py
	Image_training_overlap.py
	Image_training_pixels.py
	Image_training_rectangles.py
	MultiresHist.py
	ObjectStats.py
	Test_Photo_fromMike.py
	_init_.py
	fouriertransform.py
	imcrop.py
	preprocessing.py
**Images/**
	P10_LPS_ipsi_40x_hippo_scan_MaxIP.png
	P14_healthy_40x_hippo_scan_MaxIP.png
	P35_LPS_ipsi_40x_hippo_scan_MaxIP.png
**examples/**
	EdgeStatistics.ipynb
	Functionalized-Multires-histograms.ipynb
	Image_Unit_Tests.ipynb
	Object-Statistics.ipynb
	Test_Photo_fromMike.png
	Training_Images_Examples.ipynb
	UseCases.MD
	first-four-moments.ipynb
	fourier_transform-with-multires-hist.ipynb
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
