import numpy as np

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

def thresholding(img:np.ndarray, low:float, high:float) -> np.ndarray:
    """Thresholding the image"""
    strong = 255
    weak = 50
    m,n = img.shape
    out = np.zeros((m,n))
    print('Max/min: ', img.max(), img.min())
    print('Mean: ', img.mean())

    strong_row, strong_col = np.where(img >= high)
    weak_row, weak_col = np.where((img <= high) & (img >= low))
 
    out[strong_row, strong_col] = strong
    out[weak_row, weak_col] = weak

    return out