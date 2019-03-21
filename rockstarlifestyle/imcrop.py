# pylint: disable=W0312
# Ignoring indentation/spacing mixup. I didn't know tabs are bad
#
# Made by: Rockstar-Lifestyle | UW DIRECT | 2019
#   Team members (alphabetical): Julia Boese, Hawley Helmbrecht,
#                                   Sage Scheiwiller, David Shackelford
#
# The following py file will involve image cropping and image stack
# manipulation
#
# Note: Current version only supports png type images for stack
#       creationg; will add futher functionality later for tif and
#       tif ij images as well
#

import json
import warnings

import numpy as np

import skimage.io as sio
import tifffile


from rockstarlifestyle import multiresolution as mH



class TileData():
    """
    Creating an identifier for every tile for later use in stacking
    """
    def __init__(self, res):
        self.im_path = ''
        self.res = res
        self.data = []

    def extract_data(self,
                     path='',
                     file='',
                     filetype='.png'):
        """
        Combines full path and extracts image data
        """
        self.im_path = path + file + filetype
        self.data = sio.imread(self.im_path)

class ImgID():
    """
    Creating an identifier for every image for later use in the NN
    """
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.MRH = []
        self.GB = []
        self.bin_list = []
        self.heights = []
        self.count = []

    def calc_heights(self, plt1, plt2):
        """
        Calculates height data from plt1 and plt2
        """
        self.heights = mH.diff_hist(plt1, plt2)
    def calc_MRH(self, bins, show_figs=False):
        """
        Calculating multires histogram
        """
        if self.GB == []:
            warnings.warn("Gaussian blur needs to be performed " +
                          "before Multi Res Histogram")
        self.MRH = mH.cumulative_hist(self.GB,
                                      bins,
                                      show_figs=show_figs)
        for i in range(len(self.MRH[0][:])):
            self.bin_list.append(self.MRH[i][1])

    def calc_GB(self, gauss_blur_list):
        """
        Calculating Gaussian Blur
        """
        self.GB = mH.gauss_filter(self.data, gauss_blur_list)

def stackMRH(stacked_img):
    """
    Parameters
    ----------
    stacked_img: np.array(np.uint16) : An array of stacked data
                                       representing the images
                                       taken using the _crop) funciton

    Return
    ------
    objlist : list[objects] : list of objects with their own identifier
                              for every cropped image
    """
    bin_list = [3]
    gauss_blur_list = [0, 3]
    objlist = []
    for k in range(len(stacked_img[:, :, 0])):

        obj = ImgID(dict(
            {'Image' : '{}/{}'.format((k + 1),
                                      len(stacked_img[:, :, 0]))}),
                    stacked_img[k, :, :])
        obj.calc_GB(gauss_blur_list)
        obj.calc_MRH(bin_list, show_figs=False)
        plt1 = obj.MRH[0]
        plt2 = obj.MRH[1]
        obj.calc_heights(plt1, plt2)
        objlist.append(obj)
    return objlist

def stackLoad(path='', file=''):
    """
    The following function loads the given cropped stacked image into a
    numpy array
    Parameters
    ----------
    path: str : String of path of file in the form of r"C:/.../.../"
    file: str : String of file name

    Return
    ------
    An (n, res_x, res_y) array of n stacks of cropped images
    """
    return sio.imread('{}{}.tif'.format(path, file))


def imgCrop(path='',
            file='',
            filetype='.png',
            res=(256, 256)):
    """
    The following function acts as a wrapper for the entire py file. It
    will input an image file and given resolution and output a stacked
    set of cropped tif images. It also saves the set into a tif image
    set on the current folder

    * Current notes: I only have this running for a png input for the
                     purposes of our project, it will only output the
                     green band of the images

    Parameters
    ----------
    path: str : String of path of file in the form of r"C:/.../.../"
    file: str : String of file name to crop
    filetype: str : Type of file - only use '.png' or '.tif'
    res: int tuple : resolution (res_x, res_y) in pixels of
                     cropped image

    Return
    ------
    img_stack : np.uint16 : (n, res_x, res_y) array of n stacks of
                            cropped images
    """

    def _img_save(tile_data, stacked_img):
        """
        The following private function saves the given image array to
        a tif file with given metadata

        Parameters
        ----------
        tile_data : object : TileData() object containing required data

        Return
        ------
        stacked_img : np.uint16 : (n, res_x, res_y) array of n stacks
                                  of cropped images
        """
        metadata = json.dumps({"res" : tile_data.res,
                               "orig_Img" : tile_data.file,
                               "dtype" : stacked_img.dtype.str})

        img_j = False # For future work with tif img_j filetypes
        if img_j:
            metadata = {"Info": metadata}
        tifffile.imsave('{}stack_crop_RES{}_{}{}'.format(tile_data.path,
                                                         tile_data.res,
                                                         tile_data.file,
                                                         '.tif'),
                        stacked_img,
                        metadata=metadata,
                        imagej=img_j)

    def _crop(tile_data):
        """
        The following private function crops an image attached to
        object tile_data based on its applied resolution

        Parameters
        ----------
        tile_data: object : TileData() object containing required data

        Return
        ------
        img_stack : np.uint16 : (n, res_x, res_y) array of n stacks of
                                cropped images
        """

        img_list = []
        # Change this to change RGB band (0 == R; 1 == G; 2 == B)
        _img = tile_data.data[:, :, 1]
        res_x = tile_data.res[0]
        res_y = tile_data.res[1]

        offset = tile_data.res

        border = ((len(_img[:, 0]) % res_x)//2,
                  (len(_img[0, :]) % res_y)//2)

        img_crop = np.zeros(shape=tile_data.res, dtype='uint16')
        img_stack = np.zeros(shape=(0, 0, 0, 0), dtype='uint16')

        for j in range(len(_img[0, :])//res_x):
            for i in range(len(_img[:, 0])//res_y):
                # img_loc ='({}:{},{}:{})'.format(i*offset[0]+border[0],
                #           i*offset[0]+border[0]+offset[0],
                #           j*offset[1]+border[1],
                #           j*offset[1]+border[1]+offset[1])
                first_val = offset[0]+border[0]
                second_val = offset[1]+border[1]
                img_crop = _img[
                    i*offset[0]+border[0] : i*offset[0]+first_val,
                    j*offset[1]+border[1] : j*offset[1]+second_val
                    ]
                img_list.append(img_crop)
        img_stack = np.swapaxes(np.dstack(img_list), 2, 0)
        img_stack = np.swapaxes(img_stack, 2, 1)
        return img_stack

    assert len(res) == 2, "Input resolution can only be 2 values"

    if filetype != '.png':
        warnings.warn("The input filetype needs to be a .png for " +
                      "the current version. This will change in " +
                      "future versions")
        filetype = '.png'

    stacked_img = np.zeros(shape=(0, 0, 0, 0), dtype='uint16')

    tile_data = TileData(res)
    tile_data.extract_data(path, file, filetype)
    stacked_img = _crop(tile_data)
    return stacked_img

