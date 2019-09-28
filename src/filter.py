from scipy import ndimage
from scipy import misc

"""
Filtering methods.
"""

# Gaussian filter
face = misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)

# Uniform filter
local_mean = ndimage.uniform_filter(face, size=11)

# Sharpen
face = misc.face(gray=True).astype(float)
blurred_f = ndimage.gaussian_filter(face, 3)

# Increase edge weight
filter_blurred_f = ndimage.gaussian_filter(blurred_f, 1)
alpha = 30
sharpened = blurred_f + alpha * (blurred_f - filter_blurred_f)
