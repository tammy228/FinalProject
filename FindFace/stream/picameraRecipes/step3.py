import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
try:
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        cv2.imshow('frame', frame)
        #cv2.imshow('gray', gray)
        
        cv2.waitKey(0)
except KeyboardInterrupt:
    pass


cap.release()
cv2.destroyAllWindows()
