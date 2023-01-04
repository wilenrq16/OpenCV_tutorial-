import numpy
import cv2

img = cv2.imread("tomatoes.jpg", 1)
cv2.imshow("original", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV) # 25 shows reddish colors
cv2.imshow("Thresh", thresh)

#canny edges

edges = cv2.Canny(img, 100, 70)
cv2.imshow("canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows