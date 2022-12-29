import numpy as np
import cv2
import random

canvas = np.ones([500,500,3],'uint8')*255

#circle params
color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
line_width = -1 #filled
radius = 5
point = (-100,-100)
pressed = False

#for clicking
def click(event, x, y, flags, param): 
    global point, pressed, color, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, (x,y), radius, color, line_width)

    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(canvas, (x,y), radius, color, line_width)
    
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False

#refer to the window to recognize the mouse clicks
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click)

#white box
#white = np.ones([500,500,3], 'uint16') #white is when the value is max = 255
#white *= (2**16-1) #2 power of 16 - 1 = 255 

while(True):
    #cv2.circle(canvas, point, radius, color, line_width)
    cv2.imshow("Frame", canvas)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'): #0xFF for 64bit machine
        break
    elif ch & 0xFF == ord('c'): #0xFF for 64bit machine
        color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))

cv2.waitKey(0)
cv2.destroyAllWindows()