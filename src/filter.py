import numpy as np

from scipy import misc, ndimage

"""
Filtering methods.
"""
face = misc.face(gray=True)
f = misc.face(gray=True)
f = f[230:290, 220:320]

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

# Denoise
noisy = f + 0.4 * f.std() * np.random.random(f.shape)
gauss_denoised = ndimage.gaussian_filter(noisy, 2)
med_denoised = ndimage.median_filter(noisy, 3)
im = np.zeros((20, 20))
im[5:-5, 5:-5] = 1
im = ndimage.distance_transform_bf(im)
im_noise = im + 0.2 * np.random.randn(*im.shape)
im_med = ndimage.median_filter(im_noise, 3)

# Structure an element
el = ndimage.generate_binary_structure(2, 1)

# Erosion
a = np.zeros((7,7), dtype=np.int)
ndimage.binary_erosion(a).astype(a.dtype)
ndimage.binary_erosion(a, structure=np.ones((5,5))).astype(a.dtype)

# Dilation
ndimage.binary_dilation(a).astype(a.dtype)

# Opening
ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int)

# Application
square = np.zeros((32, 32))
square[10:-10, 10:-10] = 1
np.random.seed(2)
x, y = (32*np.random.random((2, 20))).astype(np.int)
square[x, y] = 1
open_square = ndimage.binary_opening(square)
eroded_square = ndimage.binary_erosion(square)
reconstruction = ndimage.binary_propagation(eroded_square, mask=square)
