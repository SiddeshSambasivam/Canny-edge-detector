import numpy as np

class InvalidDimensionsError(Exception):
    """Raised when image dimensions are invalid"""
    pass

class MultiChannelError(Exception):
    """Raised when image is not a single channel"""
    pass

def convolve(image: np.ndarray, kernel:np.ndarray, verbose:bool=False) -> np.ndarray:
    """Convolve image with a kernel"""
    w, h = image.shape
    k_w, k_h = kernel.shape

    if w < k_w or h < k_h:
        raise InvalidDimensionsError("Kernel dimensions must be smaller than image dimensions")
    
    if len(image.shape) != 2:
        raise MultiChannelError("Image must be a single channel")

    convolved_image = np.zeros((w, h))
    for i in range(w-k_w+1):
        for j in range(h-k_h+1):
            convolved_image[i+1][j+1] = np.sum(np.multiply(image[i:i+3, j:j+3], kernel))

    return convolved_image
    