import unittest

from canny_edge_detector import ImageHandler, canny


class TestCannyEdgeDetection(unittest.TestCase):

    path = './tests/data/test.jpeg'
    ih = ImageHandler(path, 0)
    
    def test_canny_edge_detection(self):

        out = canny(self.ih.img, verbose=True, save_outputs=True)
    