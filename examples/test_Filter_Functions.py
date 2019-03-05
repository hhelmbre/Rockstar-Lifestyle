image = Image.open('Test_Photo_fromMike.png')
radius = 80


def test_high_pass_filter(image, radius):
    """takes an image and modifiable radius and performs a forier transform and outputs an image that has a high pass filter applied"""
    fourier_fshift(image)
    assert isinstance(image, image), "input is the wrong form"
    hpf_image = Filter_functions.py()
    return hpf_image

def HPF_compare(image, radius):
    """Plots the image and the high pass filter image for comparison"""
    high_pass_filter(image, radius)
    return
