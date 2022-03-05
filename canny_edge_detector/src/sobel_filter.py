import numpy as np
from typing import List

def sobel_kernels() -> List[np.ndarray]:
    Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)
    Gx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=np.float32)
    
    return Gx, Gy

def sobel_filter(img: np.ndarray, degree:bool=True) -> List[np.ndarray]:

    Gx, Gy = sobel_kernels()
    m,n = img.shape
    grad_intensity = np.zeros((m,n))
    grad_direction = np.zeros((m,n))

    # TODO: Implement padding
    for i in range(m-2):
        for j in range(n-2):
            gx = np.sum(np.multiply(img[i:i+3, j:j+3], Gx))
            gy = np.sum(np.multiply(img[i:i+3, j:j+3], Gy))
            grad_intensity[i+1][j+1] = np.sqrt(gx**2 + gy**2)
            grad_direction[i+1][j+1] = np.arctan2(gx, gy)

    if degree:
        grad_direction = np.rad2deg(grad_direction)

    return grad_intensity, grad_direction