import unittest
from canny_edge_detector import gaussian_filter, sobel_filter, ImageHandler

import matplotlib.pyplot as plt

class TestCannyFilter(unittest.TestCase):

    path = './tests/data/test2.jpeg'
    ih = ImageHandler(path, 0)
    Gx = None
    Gy = None

    def test_gaussian_filter(self):
        img = gaussian_filter(self.ih.img, 1.4)
        plt.imsave('gaussian_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        self.ih.img = img

    def test_sobel_filter(self):

        img, direc = sobel_filter(self.ih.img)
        assert img.shape == self.ih.img.shape
        print(direc)

        plt.imsave('./tests/output/sobel_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        plt.imsave('./tests/output/sobel_filtered_direction.png', direc, cmap=plt.get_cmap('gray')) 

    