import unittest
import canny_edge_detector as ced

class TestImageViewer(unittest.TestCase):

    ih = ced.ImageHandler('./tests/data/test.jpeg', 0)

    def test_image_viewer(self):
        assert self.ih.shape == (800, 800)

    def test_image_resize(self):
        resized_img = self.ih.resize(25)
        assert resized_img.shape == (200, 200)






        
