import rawpy
import imageio

path = "image/IMG_3766.dng"
with rawpy.imread(path) as raw:
    rgb = raw.postprocess()
imageio.imsave("image/IMG_3766.tiff", rgb)
