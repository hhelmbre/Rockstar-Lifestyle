#Purpose: For functions that perform pre-processessing of images
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
from matplotlib import pyplot as plt
import scipy

def color_split():
    pass

#Function X: To change image contrast
def im_contrast(image, contrast_value)
    img = Image.fromarray(image)
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    enhanced_im = enhancer.enhance(contrast_value)
    return enhanced_im
