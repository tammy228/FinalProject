#from picamera.array import PiRGBArray
import picamera
import time
import cv2
import sys
import imutils
from imutils.video import VideoStream
from imutils import face_utils
import io
import numpy as np

saveRoute = '~/Pictures/'

haarObject = "frontalface"
haarVersion = "default"
cascPath = "haarcascades/haarcascade_" + haarObject + "_" + haarVersion + ".xml"
face_cascade = cv2.CascadeClassifier(cascPath)

#rawCapture = io.BytesIO() #Create a memory stream so photos doesn't need to be saved in a file

with picamera.PiCamera() as camera:
    #camera.resolution = (320, 240)
    #camera.start_preview()
    vs = VideoStream(usePiCamera=True).start()
    
    time.sleep(2) #camera warm-up time

    #rawCapture = PiRGBArray(camera, size=(320, 240))

    
    #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        #camera.capture(rawCapture, format = 'jpeg')
        #buff = np.fromstring(rawCapture.getvalue(), dtype=np.uint8)
        #img = cv2.imdecode(buff, 1)
        # check rawCapture    
        #print('\n\nCaptured %d x %d image\n\n' % (rawCapture.array.shape[1], rawCapture.array.shape[0]))
        print("\n\n++++++++++++++++++++++\n\n")
        #rawCapture.truncate()
        #rawCapture.seek(0)
        #img = frame.array
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_rects = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
            )

        num=1
        for(x,y,w,h) in face_rects:
            x1=x
            y1=y
            x2=x+w
            y2=y+h
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 193, 193), 1)
            grayShot = gray_img[y1:y2, x1:x2]
            cv2.imwrite(saveRoute+num+'.jpg', grayShot)
            num+=1
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

cv2.destroyAllWindows()
vs.stop()
