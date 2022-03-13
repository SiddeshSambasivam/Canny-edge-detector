import numpy as np
from typing import Type
from .ops import convolve

def generate_gaussian_filter(size: int, sigma:float) -> Type[np.ndarray]:
    """
    Generate a matrix with the Gaussian function with mean 0 and standard deviation sigma.

    Reference: https://en.wikipedia.org/wiki/Gaussian_function
    """
    axs = np.linspace(-(size//2), size//2, size)            
    xv, yv = np.meshgrid(axs, axs)
    
    PI = np.pi
    sig_sq = np.square(sigma)
    mean = 0 

    x = np.exp(-0.5*np.square(xv-mean)/sig_sq)
    y = np.exp(-0.5*np.square(yv-mean)/sig_sq)
    
    g = (x*y) * (1/(2*PI*sig_sq))
            
    return g

def gaussian_filter(img: np.ndarray, kernel_size:int=9, sigma:float=1.4) -> Type[np.ndarray]:
    """Apply a Gaussian filter to the image with kernel size and standard deviation sigma."""
    g = generate_gaussian_filter(kernel_size, sigma)
    img = convolve(img, g)

    return img
