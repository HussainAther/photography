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
