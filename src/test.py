import imageio
import matplotlib as mpl
import PIL
import rawpy

from matplotlib.pyplot import imsho

path = "image/IMG_3766.dng"
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
imageio.imsave("image/IMG_3766.tiff", rgb)
