import cv2
import numpy as np
from typing import Type

def generate_gaussian_filter(nx: int, ny:int, sigma:float) -> Type[np.ndarray]:
    x = np.linspace(-(nx//2), nx//2, nx)            
    y = np.linspace(-(ny//2), ny//2, ny)

    xv, yv = np.meshgrid(x, y)
    g = np.exp(-(xv**2 + yv**2) / (2 * sigma**2))
            
    return (1/(2*np.pi*sigma**2))*g

def gaussian_filter(img: np.ndarray, sigma:float) -> Type[np.ndarray]:
    g = generate_gaussian_filter(5, 5, sigma)
    img = cv2.filter2D(img, -1, g)

    return img
