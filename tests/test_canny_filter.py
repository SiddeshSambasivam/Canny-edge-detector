import unittest
import pickle
import cv2

from pytest import skip
from canny_edge_detector import ImageHandler, canny, non_max_suppression


class TestCannyEdgeDetection(unittest.TestCase):

    path = './tests/data/chess.png'
    ih = ImageHandler(path, 0)

    @unittest.skip("Skipping test_non_max_suppression")
    def test_non_max_suppression(self):

        with open('./tests/pkl/gradient_magnitude.pkl', 'rb') as f:
            gradient_magnitude = pickle.load(f)

        with open('./tests/pkl/gradient_direction.pkl', 'rb') as f:
            gradient_direction = pickle.load(f)

        suppr_image = non_max_suppression(gradient_magnitude, gradient_direction)
    
    def test_canny_edge_detection(self):

        # out = canny(self.ih.img, verbose=True, save_outputs=True, subpixel_correction=True)
        img = self.ih.resize(25)
        out = canny(img, verbose=True, save_outputs=True, subpixel_correction=False)

        out = cv2.resize(out, (self.ih.shape[1], self.ih.shape[0]), interpolation = cv2.INTER_AREA)
        # out = self.ih.resize(out)
        # save the output
        self.ih.save_image(out, './tests/data/chess_canny.png')

