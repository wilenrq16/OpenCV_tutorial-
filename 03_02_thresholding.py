import numpy as np
import cv2

bw = cv2.imread('detect_blob.png', 0) #0 reads it as black and white
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height,width,1], 'uint8') #1 indicates there is one channel binary image (bw)


# can be change 
thresh = 117  #85 is the threshold if it goes black or white
thresh2 = 85

for row in range (0, height): #each row of the image is the height of the image
    for col in range (0, width): #each col of the image is the width of the image
        if bw[row][col]>thresh:
            binary[row][col]=255

cv2.imshow("Slow Binary", binary)

#faster way to set threshold
ret, thresh2 = cv2.threshold(bw,thresh2,255,cv2.THRESH_BINARY)
cv2.imshow("OpenCV thresh", thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows
