import numpy as np

from scipy import misc, ndimage

"""
Feature extraction
"""

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1

im = ndimage.rotate(im, 15, mode="constant")
im = ndimage.gaussian_filter(im, 8)

# Sobel gradient operator
sx = ndimage.sobel(im, axis=0, mode="constant")
sy = ndimage.sobel(im, axis=1, mode="constant")
sob = np.hypot(sx, sy)
