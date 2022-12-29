import numpy as np
import cv2

black = np.zeros([150,200,1], 'uint8') #creates 150x200 image
cv2.imshow("Black", black) # shows the image into a window
print(black[0,0,:]) #prints the value @ [0,0]

ones = np.ones([150,200,3], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0,0,:])

white = np.ones([150,200,3], 'uint16') #white is when the value is max = 255
white *= (2**16-1) #2 power of 16 - 1 = 255 
cv2.imshow("White", white)
print(white[0,0,:]) #should print 255

color = ones.copy()
color[:,:] = (255,0,0) #(b,r,g) maxing out the b
cv2.imshow("Blue", color)
print(color[0,0,:])

cv2.waitKey(0) #waiting for a key interrupt
cv2.destroyAllWindows() #closes all windows
