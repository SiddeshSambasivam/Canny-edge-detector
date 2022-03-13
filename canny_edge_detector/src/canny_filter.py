import os
import numpy as np
import matplotlib.pyplot as plt
import copy

from .gaussian_filter import gaussian_filter
from .sobel_filter import sobel_filter

STRONG = 255
WEAK = 50

def non_max_suppression(mag_mat, dir_mat:np.ndarray) -> np.ndarray: 
    """Makes the edges thinner"""

    m,n = dir_mat.shape
    out = np.zeros((m,n))

    for i in range(1, m-1):
        for j in range(1, n-1):
            ang = dir_mat[i][j]
            if (0 <= ang  < 22.5) or (337.5 <= ang <= 360) or (157.5 <= ang <= 202.5):
                pos = mag_mat[i][j+1]
                neg = mag_mat[i][j-1]
            elif (67.5 <= ang < 112.5) or (247.5 <= ang < 292.5):
                pos = mag_mat[i-1][j]
                neg = mag_mat[i+1][j]
            elif (112.5 <= ang < 157.5) or (292.5 <= ang < 337.5):
                pos = mag_mat[i-1][j-1]
                neg = mag_mat[i+1][j+1]
            else:
                # NOTE: This corresponds to this case = (22.5 <= ang < 67.5) or (202.5 <= ang < 247.5)
                pos = mag_mat[i-1][j+1]
                neg = mag_mat[i+1][j-1]
            
            if mag_mat[i][j] >= pos and mag_mat[i][j] >= neg:
                out[i][j] = mag_mat[i][j]
    
    return out

def thresholding(img:np.ndarray, low:float, high:float, verbose:bool=False) -> np.ndarray:
    """
    Thresholding the image using the given low and high values.

    Parameters
    ----------
    img : np.ndarray
        Image to be thresholded
    low : float
        Lower cutoff value
    high : float
        Higher cutoff value
    strong : int, optional
        Strong threshold value is set for pixel values greater than high. The default is 255.
    weak : int, optional
        Weak threshold value is set for pixel values in the [high, low]. The default is 50.
    verbose : bool, optional
        Whether to print the thresholding values. The default is False.
    
    Returns
    -------
    out : np.ndarray
        The output of thresholding
    
    """
    m,n = img.shape
    out = np.zeros((m,n))

    if verbose:
        print('\nMax/min: ', img.max(), img.min())
        print('Mean: ', img.mean())

    strong_row, strong_col = np.where(img >= high)
    weak_row, weak_col = np.where((img <= high) & (img >= low))
 
    out[strong_row, strong_col] = STRONG
    out[weak_row, weak_col] = WEAK

    return out

def blob_analysis(image:np.ndarray, outer_range:range, inner_range:range) -> np.ndarray:
    """
    Filters a weak edge pixel by looking at its 8-connected neighborhood pixels and decides if it should be strong or discarded.

    Strong pixels are set to 255 and weak pixels are set to 0.

    NOTE: This function is used in hysteresis to filter weak pixels. 

    Parameters
    ----------
    image : np.ndarray
        Image to be processed
    outer_range : range
        Range of outer indices
    inner_range : range
        Range of inner indices
        
    Returns
    -------
    out : np.ndarray
        The output of blob filter
    """

    for i in outer_range:
        for j in inner_range:
            if image[i][j] == WEAK:
                if image[i-1][j-1] == STRONG or image[i-1][j] == STRONG \
                    or image[i-1][j+1] == STRONG or image[i][j-1] == STRONG \
                        or image[i][j+1] == STRONG or image[i+1][j-1] == STRONG \
                            or image[i+1][j] == STRONG or image[i+1][j+1] == STRONG:
                    image[i][j] = STRONG
                else:
                    image[i][j] = 0    

    return image

def hysteresis(image:np.ndarray) -> np.ndarray:
    """
    Checks for hysteresis in the image and normalizes the output

    NOTE: There are two cases that happens during hysteresis:
    1. When traversing from left to right, weak pixels to the right are preserved but weak pixels to the left are discarded
    2. When traversing from right to left, weak pixels to the left are preserved but weak pixels to the right are discarded

    Therefore the output of both traversals are added together and then normalized to the range [0, 255].

    Parameters
    ----------
    image : np.ndarray
        Image to be processed

    Returns
    -------
    out : np.ndarray
        The output of hysteresis    
     
    """
    image_right = copy.deepcopy(image)
    image_left = copy.deepcopy(image)
    m,n = image.shape

    image_right = blob_analysis(image_right, range(1, m), range(1, n))
    image_left  = blob_analysis(image_left, range(m-1, 0, -1), range(n-1, 0, -1))

    out = image_right + image_left
    out[out > 255] = 255

    return out

def canny(image:np.ndarray, low:float=10, high:float=30, verbose:bool=False, save_outputs:bool=False) -> np.ndarray:
    """Canny edge detection is a technique for finding edges in an image.
    Parameters
    ----------
    image : np.ndarray
        Image to be processed
    low : float, optional
        Lower cutoff value. The default is 10.
    high : float, optional
        Higher cutoff value. The default is 30.
    verbose : bool, optional
        Whether to print the thresholding values. The default is False.
    
    Returns
    -------
    out : np.ndarray
        The output of canny edge detection
    
    """

    denoised_image = gaussian_filter(image) 
    
    
    gradient_magnitude, gradient_direction = sobel_filter(denoised_image, verbose) 

    suppr_image = non_max_suppression(gradient_magnitude, gradient_direction)
    thers = thresholding(suppr_image, low, high, verbose)

    out = hysteresis(thers)

    if save_outputs:

        # check if outputs folder exists
        if not os.path.exists('./outputs'):
            os.makedirs('./outputs')

        plt.imsave('./outputs/1_gaussian_filtered.png', denoised_image, cmap=plt.get_cmap('gray'))
        plt.imsave('./outputs/2_sobel_filtered.png', gradient_magnitude, cmap=plt.get_cmap('gray'))
        plt.imsave('./outputs/3_non_max_suppression.png', suppr_image, cmap=plt.get_cmap('gray')) 
        plt.imsave('./outputs/4_thresholding.png', thers, cmap=plt.get_cmap('gray')) 
        plt.imsave('./outputs/5_hysteresis.png', out, cmap=plt.get_cmap('gray'))
    
    return out