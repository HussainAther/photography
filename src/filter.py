from scipy import ndimage
from scipy import misc

"""
Filtering methods.
"""

# Gaussian filter
face = misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)
