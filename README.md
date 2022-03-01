Canny edge detector
================================

## Algorithm
The process of Canny edge detection algorithm can be broken down to five different steps:

<p align="center">
    <img src="./assets/canny_algorithm.png" width="500px">
</p>

1. Apply Gaussian filter to smooth the image in order to remove the noise
2. Find the intensity gradients of the image
3. Apply gradient magnitude thresholding or lower bound cut-off suppression to get rid of spurious response to edge detection
4. Apply double threshold to determine potential edges
5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.

## Requirements

1. Take pictures of a B&W chessboard at a high resolution (eg. 3000x4000)
2. Apply your Canny edge detector to these images (grey only) with accuracy to pixel level (integer)
3. Reduce the size to ¼ of the original image (eg 750x1000), then apply the Canny edge detector with sub-pixel accuracy. The output is a list of edge pixels with decimal points numbers. 
Casting these edge pixels to its original size of 3000x4000 and make a comparison with the results obtained in 2. Discrepancies can be presented in the report/during the face-to-face assessment.
4. Repeat the above to photos with daily life settings.

## Technical specs

1. Image handler

    Handles all the basic operations on an image

    Eg. Loads the image, saves the image, resize the image

2. Canny edge detector (Refer to the algorithm)

## Development

1. Setup the dev environment

    *Prereq: Miniconda was used to setup the development environment.*

    ```bash
    > conda create --name canny python=3.8
    > conda activate canny
    > pip install -r requirements.txt
    ```

2. Run the tests 

    ```bash
    > pytest -v
    ```
