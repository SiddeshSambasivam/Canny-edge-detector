import unittest
from canny_edge_detector import gaussian_filter, sobel_filter, \
    ImageHandler, convolve, sobel_kernels, non_max_suppression 

import matplotlib.pyplot as plt
from canny_edge_detector.src.canny_filter import thresholding


class TestCannyFilter(unittest.TestCase):

    path = './tests/data/test2.jpeg'
    ih = ImageHandler(path, 0)
    
    @unittest.skip("Skipped")
    def test_gaussian_filter(self):
        img = gaussian_filter(self.ih.img, 3)
        plt.imsave('./tests/outputs/gaussian_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        self.ih.img = img

    @unittest.skip("Skipped")
    def test_convolution(self):
        img = self.ih.img
        gx, _ = sobel_kernels()
        out = convolve(img, gx)
        assert out.shape == img.shape

    @unittest.skip("Skipped") 
    def test_sobel_filter(self):

        img, direc = sobel_filter(self.ih.img)
        assert img.shape == self.ih.img.shape

        plt.imsave('./tests/outputs/sobel_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        plt.imsave('./tests/outputs/sobel_filtered_direction.png', direc) 
    
    @unittest.skip("Skipped")
    def test_non_max_suppression(self):
        
        img, direc = sobel_filter(self.ih.img, True) 
        out = non_max_suppression(img, direc)
        plt.imsave('./tests/outputs/non_max_suppression.png', out, cmap=plt.get_cmap('gray')) 

    def test_double_threshold(self):

        img = gaussian_filter(self.ih.img) 
        plt.imsave('./tests/outputs/1_gaussian_filtered_image.png', img, cmap=plt.get_cmap('gray'))
        
        img, direc = sobel_filter(img, True) 
        plt.imsave('./tests/outputs/2_sobel_filtered_image.png', img, cmap=plt.get_cmap('gray'))

        out = non_max_suppression(img, direc)
        plt.imsave('./tests/outputs/3_non_max_suppression.png', out, cmap=plt.get_cmap('gray')) 

        thers = thresholding(out, 5, 20, True)
        plt.imsave('./tests/outputs/4_double_thresholding.png', thers, cmap=plt.get_cmap('gray')) 


    
    