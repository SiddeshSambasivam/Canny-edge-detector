import numpy as np

class InvalidDimensionsError(Exception):
    """Raised when image dimensions are invalid"""
    pass

class MultiChannelError(Exception):
    """Raised when image is not a single channel"""
    pass

def convolve(image: np.ndarray, kernel:np.ndarray, verbose:bool=False) -> np.ndarray:
    """Convolutes the image with the kernel."""
    w, h = image.shape
    k_w, k_h = kernel.shape

    if w < k_w or h < k_h:
        raise InvalidDimensionsError("Kernel dimensions must be smaller than image dimensions")
    
    if len(image.shape) != 2:
        raise MultiChannelError("Image must be a single channel")

    # Reference: http://d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html
    padded_image = np.zeros((w+k_w-1, h+k_h-1))
    padded_image[k_w//2:w+k_w//2, k_h//2:h+k_h//2] = image

    convolved_image = np.zeros((w, h))
    for i in range(w):
        for j in range(h):
            convolved_image[i][j] = np.sum(np.multiply(padded_image[i:i+k_w, j:j+k_h], kernel))
    
    if verbose:
        print(f"\nImage dim: {image.shape[0]}x{image.shape[1]}")
        print(f"Kernel dim: {kernel.shape[0]}x{kernel.shape[1]}")
        print(f"Padded image dim: {padded_image.shape[0]}x{padded_image.shape[1]}")
        print(f"Convolved image dim: {convolved_image.shape[0]}x{convolved_image.shape[1]}")    

    return convolved_image
