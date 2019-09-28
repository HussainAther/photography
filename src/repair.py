import rawpy.enhance

"""
Repair bad/dead pixels in RAW files.
"""

paths = ["image1.nef", "image2.nef", "image3.nef"]
bad_pixels = rawpy.enhance.find_bad_pixels(paths)

for path in paths:
    with rawpy.imread(path) as raw:
        rawpy.enhance.repair_bad_pixels(raw, bad_pixels, method="median")
        rgb = raw.postprocess()
    imageio.imsave(path + ".tiff", rgb)
