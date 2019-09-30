import numpy as np
import cv2

"""
Harris corner detection.
"""

# Read image
img = cv2.imread("image/octagon.png")
cv2.imshow("Image", img)

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", img_gray)

# Compute Harris corner detector response (params: block size, Sobel aperture, Harris alpha)
h_response = cv2.cornerHarris(img_gray, 2, 3, 0.04)
h_min, h_max, _, _ = cv2.minMaxLoc(h_response)  # for thresholding, display scaling
#print "Harris response: [min, max] = [{}, {}]".format(h_min, h_max)  # [debug]
cv2.imshow("Harris response", np.uint8((h_response - h_min) * (255.0 / (h_max - h_min))))
