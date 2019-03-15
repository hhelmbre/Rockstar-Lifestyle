#Purpose: To perform the fourier transform
#import necessary packages
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance

#Function 1: Performs the fourier transform with steps to get Magnitude_Spectrum
#Steps: fourier transform, fourier shift, gets the magnitude Spectrum
#Inputs: image
#Outputs: magntidue spectrum array
def Magnitude_Spectrum(image):
    """Peforms a fourier transform and returns the m_spec"""
    fshift = fourier_fshift(image)
    m_spec= np.log(np.abs(fshift))
    return m_spec

#Function 2: Performs the fourier transform to get fshift
#Steps: fourier transform, fourier shift, gets the magnitude Spectrum
#Inputs: image
#Outputs: fshift
def fourier_fshift(image):
    """peforms the fourier transform and returns the fshift"""
    f = np.fft.fft2(image)
    fshift= np.fft.fftshift(f)
    return fshift

#Function 3: Plotting the magnitude spectrum made my fourier transformM
#Steps: plots the Magnitude Spectrum
#Input: the magnitude spectrum Output
#Output: none it just shows the image for funsies
# def Plot_M_Spec(m_spec):
#     plt.show(m_spec)
#     plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
#     plt.show()
#     return

#Function 4: Performs an inverse fourier transform
#Steps: unshifts the image, inverse fourier, normalizes the image
#Inputs: f_shift
#Outputs: image array of inverse fouriered image
def inverse_fourier(f_shift):
    image_revert = np.fft.ifftshift(hpf_fshift)
    image = np.fft.ifft2(image_revert)
    image = np.abs(image)
    return image
