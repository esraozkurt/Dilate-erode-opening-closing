# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U-n65HSs1Mn7VebREmZUo3IJ8avCYoXR
"""

from google.colab import files
from IPython.display import Image

uploaded=files.upload()

Image('kiraz.jpg')

import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread("kiraz.jpg", 0)
cv2_imshow(img)

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread("kiraz.jpg", 0)
cv2_imshow(img)
cv2.waitKey(0)

kernel = np.ones((5, 5), dtype=np.uint8)

result = cv2.erode(img, kernel, iterations=1)
cv2_imshow(result)
cv2.waitKey(0)

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread("kiraz.jpg", 0)
cv2_imshow(img)
cv2.waitKey(0)

kernel = np.ones((5, 5), dtype=np.uint8)

result = cv2.dilate(img, kernel, iterations=1)
cv2_imshow(result)
cv2.waitKey(0)

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread("kiraz.jpg", 0)
cv2_imshow(img)
cv2.waitKey(0)

kernel = np.ones((5, 5), dtype=np.uint8)

whiteNoise = np.random.randint(0, 2, size=img.shape[:2])
whiteNoise = whiteNoise * 255
noise_img = whiteNoise + img

opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
cv2_imshow(opening)
cv2.waitKey(0)

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread("kiraz.jpg", 0)
cv2_imshow(img)
cv2.waitKey(0)

kernel = np.ones((5, 5), dtype=np.uint8)

blackNoise = np.random.randint(0, 2, size=img.shape[:2])
blackNoise = blackNoise * -255
noise_img = blackNoise + img
noise_img[noise_img <= -245] = 0

closing = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
cv2_imshow(closing)
cv2.waitKey(0)