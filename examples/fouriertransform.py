#Purpose: To perform the fourier transform

#import necessary packages
import numpy as np
from matplotlib import pyplot as plt

#Function 1: Performs the fourier transform with steps to get Magnitude_Spectrum
#Steps: fourier transform, fourier shift, gets the magnitude Spectrum
#Inputs: images
#Outputs: magntidue spectrum array
def Magnitude_Spectrum(image):
    f = np.fft.fft2(image)
    fshift= np.fft.fftshift(f)
    m_spec= np.log(np.abs(fshift))
    return m_spec

#Function 2: Plotting the magnitude spectrum made my fourier transformM
#Steps: plots the Magnitude Spectrum
#Input: the magnitude spectrum Output
#Output: none it just shows the image for funsies
def Plot_M_Spec(m_spec):
    plt.imshow(m_spec, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    return
