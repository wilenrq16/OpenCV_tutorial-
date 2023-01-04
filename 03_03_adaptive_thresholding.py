#This is helpful for having different threshold in different sections of the image
import numpy
import cv2

img = cv2.imread("sudoku.png", 0) #0 to load it as blacknwhite
cv2.imshow("Original", img)

ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1) 
cv2.imshow("AdaptiveThreshold", thresh_adapt)

cv2.waitKey()
cv2.destroyAllWindows