from picamera.array import PiRGBArray
import picamera
import time
import cv2
import sys
import imutils
import io

haarObject = "frontalface"
haarVersion = "default"
cascPath = "haarcascades/haarcascade_" + haarObject + "_" + haarVersion + ".xml"
face_cascade = cv2.CascadeClassifier(cascPath)

with picamera.PiCamera() as camera:
    rawCapture = io.BytesIO()
    camera.resolution = (800, 600)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(800, 600))
    
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # check rawCapture    
        print('\n\nCaptured %d x %d image\n\n' % (rawCapture.array.shape[1], rawCapture.array.shape[0]))
        print("\n\n++++++++++++++++++++++\n\n")
        rawCapture.truncate()
        rawCapture.seek(0)
        img = frame.array
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_rects = face_cascade.detectMultiScale(
            gray_img,
            scaleFactor=1.1,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE,
            minSize=(30,30)
            )

        for(x,y,w,h) in face_rects:
            cv2.circle(img, (x+w/2, y+h/2), int((w+h)/3), (255, 255, 255), 1)
        cv2.imshow('image', img)
        cv2.waitKey(1)
    cv2.destroyAllWindows()
