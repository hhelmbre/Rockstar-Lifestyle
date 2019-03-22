from rockstarlifestyle import imcrop as iC
import pandas as pd
import skimage
import skimage.io as sio
import random
import numpy as np


def test_stackmrh():
    """
    Testing stackmrh() function
    """
    img_stack = []
    for k in range(3):
        img_stack.append([])
        for i in range(256):
            img_stack[k].append([])
            for _ in range(256):
                integer = random.randint(0, 256)
                img_stack[k][i].append(integer)
    img_stack = np.asarray(img_stack)
    obj = iC.stackmrh(img_stack)
    assert len(obj) == 3, "Failed length check"
    assert obj[0].mrh[0][1][1]//1 == 85.0, "Failed value check"
    assert obj[2].name['Image'] == '3/3', "Failed id check"
    return



def test_img_crop():
    """
    Testing img_crop() function
    """
    file = 'P10_PAM_ipsi_40x_hippo_scan_MaxIP'
    filetype = '.png'
    path = r"../Images/"
    res_x = 256
    res_y = 256
    im_path = path + file+ filetype
    img_stack = iC.img_crop(path, file, filetype, (res_x, res_y))
    assert img_stack.shape == (280, 256, 256), "Stack is not the right proportions"
    assert img_stack.dtype == 'uint8', "Stack is not the right datatype"
    assert (img_stack[0][35] == [
        79,  72,  56,  74,  56,  51,  72,  54,  56,  54,  67,  56,  84,
        95,  54,  67,  54,  67,  51,  56,  46,  67,  64,  49,  56,  51,
        51,  82,  97,  64,  72,  72,  72, 131,  72,  74,  59,  92,  54,
        59,  77,  72,  59,  69,  61,  44,  49,  51,  59,  59,  67,  61,
        56,  67,  51,  72,  95,  79,  87,  59,  51,  54,  64,  54,  64,
        72,  92,  90,  82,  59,  72,  69,  79,  90,  72,  69,  87,  59,
        61,  69,  61,  87,  59,  82,  72,  69,  79,  59,  79,  69,  79,
        74,  61,  69,  59,  64,  90,  74, 131,  74,  87,  74,  82,  82,
        97,  67,  72,  61,  90,  69,  67,  61,  67,  84,  95,  92,  72,
        97, 110,  77,  97,  79,  72,  69,  74,  61,  69,  79,  56,  79,
        54,  56,  69,  64,  64,  72,  79,  49,  87,  74,  79,  82,  64,
        82,  64, 166, 128,  92, 102,  64,  74,  82,  67,  84,  84,  95,
        51,  74,  84,  54,  82,  69,  64,  49,  54,  77,  56,  64,  74,
        77,  54,  69,  79,  84, 102, 120,  92,  77,  84,  69,  54,  90,
        61,  59,  69,  49,  59,  77,  67,  56,  56,  69, 113,  79,  97,
        59,  90, 187,  56,  82,  56,  69,  56,  79,  56,  74,  79,  82,
       255, 236,  87,  54, 118,  67,  95, 120, 100,  79,  56,  64,  59,
        69,  69,  54,  51,  59,  87, 141, 102,  61,  56,  79,  54, 255,
        95,  92,  64, 115,  59,  90,  69,  69,  64,  92,  56,  72,  61,
        77,  74,  79,  56,  59,  79,  72,  61, 156]).min(), \
        "Random variable output came out false"

    return
