#Purpose: To perform the fourier transform

#import necessary packages
import numpy as np
#import matplotlib as plt
#matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance

#Function 1: Performs the fourier transform with steps to get Magnitude_Spectrum
#Steps: fourier transform, fourier shift, gets the magnitude Spectrum
#Inputs: images
#Outputs: magntidue spectrum array
def Magnitude_Spectrum(image):
    """peforms the fourier transform and returns the fshift which is used within filter functions"""
    fshift = fourier_fshift(image)
    m_spec= np.log(np.abs(fshift))
    return m_spec

#Function 2: Performs the fourier transform with steps to get fshift - used within filter functions
#Steps: fourier transform, fourier shift, gets the magnitude Spectrum
#Inputs: images
#Outputs: fshift
def fourier_fshift(image):
    """peforms the fourier transform and returns the fshift which is used within filter functions"""
    f = np.fft.fft2(image)
    fshift= np.fft.fftshift(f)
    return fshift

#Function 3: Plotting the magnitude spectrum made my fourier transformM
#Steps: plots the Magnitude Spectrum
#Input: the magnitude spectrum Output
#Output: none it just shows the image for funsies
def Plot_M_Spec(m_spec):
    plt.show(m_spec, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    return
