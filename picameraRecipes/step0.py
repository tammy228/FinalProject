import numpy as np
import cv2
try:
    img = cv2.imread('image00.jpg',0)
    cv2.imshow('image',img)
    cv2.waitKey(0)
except eyboardInterrupt:
    pass
cv2.destroyAllWindows()
