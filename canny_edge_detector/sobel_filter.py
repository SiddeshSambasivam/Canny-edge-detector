import numpy as np
from typing import List

from .ops import convolve

def sobel_kernels() -> List[np.ndarray]:
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    
    return Gx, Gy

def sobel_filter(img: np.ndarray, convert_to_deg:bool=False) -> List[np.ndarray]:

    Gx, Gy = sobel_kernels()
    
    gx = convolve(img, Gx, True)
    gy = convolve(img, Gy, True)

    grad_intensity = np.sqrt(np.square(gx) + np.square(gy))
    grad_intensity *= 255.0/grad_intensity.max()

    grad_direction = np.arctan2(gy, gx)

    if convert_to_deg:
        grad_direction = np.rad2deg(grad_direction)
        grad_direction += 180

    return grad_intensity, grad_direction