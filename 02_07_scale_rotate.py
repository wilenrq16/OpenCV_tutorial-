import numpy as np
import cv2

img = cv2.imread("image_night.jpg", 1)

#Scale
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (600,600))
img_sretch_near = cv2.resize(img, (600, 600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Streatch", img_stretch)
cv2.imshow("Near", img_sretch_near)

#Rotate
M = cv2.getRotationMatrix2D((150,150), -90, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()