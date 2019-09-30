import numpy as np
import cv2

"""
Harris corner detection.
"""

# Read image
img = cv2.imread("image/octagon.png")
cv2.imshow("Image", img)
