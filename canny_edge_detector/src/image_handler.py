import cv2
import numpy as np

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
