#imports for packages
import numpy as np
import matplotlib as plt
from PIL import Image, ImageFilter, ImageEnhance
#import internal packages
from RockstarLifestyle import fouriertransform


#Function 1: Test of Magnitude_Spectrum function
def test_Magnitude_Spectrum():
    """test of a function that peforms the fourier transform and returns the fshift which is used within filter functions"""
#inputs for functions
    image = Image.open('Test_Photo_fromMike.png').convert('L')
#function performance
    m_spec = fouriertransform.Magnitude_Spectrum(image)
#asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(m_spec, np.ndarray), "output is in the wrong form"
    return m_spec

#Function 2: Test of fourier_fshift
def test_fourier_fshift():
    """test of a function which performs the fourier transform and returns the fshift which is used within filter functions"""
#inputs for functions
    image = Image.open('Test_Photo_fromMike.png').convert('L')
#function performance
    fshift = fouriertransform.fourier_fshift(image)
#asserts and checks
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(fshift, np.ndarray), "output is in the wrong form"
    return fshift

# #Function 3: Test of Plot_M_Spec
# def test_Plot_M_Spec():
# #inputs for functions
#     image = Image.open('Test_Photo_fromMike.png').convert('L')
# #runs function
#     fouriertransform.Plot_M_Spec(image)
# #asserts and checks
#     assert isinstance(image, Image.Image), "input is in the wrong form"
#     return
