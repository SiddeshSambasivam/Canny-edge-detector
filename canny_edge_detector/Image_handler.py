import imp
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(path: str, channel_type:int=1) -> np.ndarray:
    """Loads an image from the given path."""
    img:np.ndarray = cv2.imread(path, channel_type)

    return img

def rescale_image(img:np.ndarray, scale_percent:float):
    """Resizes an image based on the scale percentage"""
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def get_directory_path(path: str) -> str:  
    """Returns the directory path for a given file path"""

    path = '/'.join(path.split("/")[:-1])
    return path

def save_image(img: np.ndarray, path: str) -> None:
    """Saves an image to the path"""
    
    dir_path = get_directory_path(path)    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    plt.imsave(path, img, cmap=plt.get_cmap('gray'))

class ImageHandler:

    def __init__(self, src: str, channelType:int=1) -> None:
        """
        channelType: [Color: 1, gray scale: 0, unchanged: -1]
        """
        super().__init__()

        if type(src) == str:
            self.img = cv2.imread(src, channelType)
        else:
            self.img = src 

        self.channelType = channelType
        self.shape = self.img.shape

    def resize(self, scale_percent:int) -> np.ndarray:
        """Resizes the images for the given scale percent"""
  
        width = int(self.shape[1] * scale_percent / 100)
        height = int(self.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized = cv2.resize(self.img, dim, interpolation = cv2.INTER_AREA)

        return resized

    def show(self) -> None:
        """Displays the image of the handler"""
        cv2.imshow('Image', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    @staticmethod
    def save_image(img: np.ndarray, path: str) -> None:
        cv2.imwrite(path, img)
