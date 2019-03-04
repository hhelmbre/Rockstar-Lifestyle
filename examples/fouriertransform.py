#Purpose: To perform the fourier transform

#import necessary packages
import import numpy as np

#Function 1: Performs the fourier transform with steps to get Magnitude_Spectrum
def Magnitude_Spectrum(image):
    f = np.fft.fft2(image)
    fshift= np.fft.fftshift(f)
    m_spec= np.log(np.abs(fshift))
    return m_spec

#Function 2: Plotting the magnitude spectrum made my fourier transformM
def Plot_M_Spec(m_spec):
        plt.imshow(m_spec, cmap = 'gray')
        plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
        plt.show()
        return
