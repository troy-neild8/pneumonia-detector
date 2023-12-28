import pydicom as dicom

import numpy as np

import cv2

ds = dicom.dcmread(
    "rsna-pneumonia-detection-challenge/stage_2_train_images/153dc47f-9a10-4cbe-a0eb-8a747cc6d8b8.dcm"
)  # read dcm extension image

img = np.asarray(ds.pixel_array)  # shape = (height, width)

img = np.expand_dims(img, axis=0)  # shape = (1,height, width)

img = np.moveaxis(img, -1, 0)  # shape = (height, 1, width)

# shape = (height, width, 1) -> gray scale image array (1 channel)
img = np.moveaxis(img, -1, 0)

# # shape = (height, width, 3) -> color image array(3 channel)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

cv2.imwrite("output.jpg", img)  # save image in jpg format
