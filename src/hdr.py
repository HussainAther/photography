import numpy as np

"""
High dynamic range
"""

def readImagesAndTimes():
  # List of exposure times
  times = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
  # List of image filenames
  filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]
  images = []
  for filename in filenames:
    im = cv2.imread(filename)
    images.append(im)
  return images, times

# Align input images
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

# Obtain Camera Response Function (CRF)
calibrateDebevec = cv2.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(images, times)

# Merge images into an HDR linear image
mergeDebevec = cv2.createMergeDebevec()
hdrDebevec = mergeDebevec.process(images, times, responseDebevec)
# Save HDR image.
cv2.imwrite("hdrDebevec.hdr", hdrDebevec)
