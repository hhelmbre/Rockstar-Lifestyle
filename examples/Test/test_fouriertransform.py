import numpy as np
import matplotlib as plt
from PIL import Image, ImageFilter, ImageEnhance
import fouriertransform


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
#
# #Function 3: Test of Plot_M_Spec
# def test_Plot_M_Spec(m_spec):
#     plt.imshow(m_spec, cmap = 'gray')
#     plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#     plt.show()
#     return
#

#Function 4: Test of color_split
def test_color_split():
    """test of a function which splits the image into r or g or b color frequency then performs a fshift for that color"""
# inputs for the function
    image = Image.open('Test_Photo_fromMike.png')
    desired_color = 'b'
#function performance
    fshift = fouriertransform.color_split(image, desired_color)
#asserts and checks
    assert isinstance(desired_color, str), "input needs to be a string called r or g or b"
    assert isinstance(image, Image.Image), "input is in the wrong form"
    assert isinstance(fshift, np.ndarray), "output is in the wrong form"
    return(fshift)
