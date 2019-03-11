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


#Function 4: Splits the image into rgb components and creates shifts and magnitudes for them
#Steps: split into components, used inputs with if tree to create shifts and magnitude for desired color
#Input: desired color and image
#Output: desired color fshift
def color_split(image, desired_color):
    """splits the image into r or g or b color frequency then performs a fshift for that color"""
#splits the image into the rbg componetnts
    image_color = Image.open('Test_Photo_fromMike.png')
    r,g,b = image_color.split()
#if tree split based on desired color
    if desired_color == "b":
    #creates shift for blue
        f_blue = np.fft.fft2(b)
        fshift_blue = np.fft.fftshift(f_blue)
        m_spec_blue = np.log(np.abs(fshift_blue))
        fshift = fshift_blue
    elif desired_color == "g":
    #creates shift for green
        f_green = np.fft.fft2(g)
        fshift_green = np.fft.fftshift(f_green)
        m_spec_green = np.log(np.abs(fshift_green))
        fshift = fshift_green
    elif desire_color == "r":
    #creates shfit for red
        f_red = np.fft.fft2(g)
        fshift_red = np.fft.fftshift(f_red)
        m_spec_red = np.log(np.abs(fshift_red))
        fshift = fshift_red
    #encompasses the rest of the inputs that do not work
    else:
         print('that desired color is not available')
    return(fshift)
