import unittest
from canny_edge_detector import gaussian_filter, sobel_filter, ImageHandler

import matplotlib.pyplot as plt

class TestCannyFilter(unittest.TestCase):

    path = './tests/data/test2.jpeg'
    ih = ImageHandler(path, 0)
    
    def test_gaussian_filter(self):
        img = gaussian_filter(self.ih.img, 1.4)
        plt.imsave('./tests/outputs/gaussian_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        self.ih.img = img

    @unittest.skip("Takes longer time")
    def test_sobel_filter(self):

        img, direc = sobel_filter(self.ih.img)
        assert img.shape == self.ih.img.shape

        plt.imsave('./tests/outputs/sobel_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        plt.imsave('./tests/outputs/sobel_filtered_direction.png', direc, cmap=plt.get_cmap('gray')) 
    
    def test_non_max_suppression(self):
        
        img, direc = sobel_filter(self.ih.img) 
        m,n = direc.shape

    