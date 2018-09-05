from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--picamera", type=int, default=-1,
        help="whether or not hte Raspberry Pi camera should be used")
args = vars(ap.parse_args())
print("[INFO] camera sensor warming up...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

haarObject = "frontalface"
haarVersion = "default"
cascPath = "haarcascades/haarcascade_" + haarObject + "_" + haarVersion + ".xml"
face_cascade = cv2.CascadeClassifier(cascPath)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=480)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rects = faceCascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
    (x, y, w, h) in faces_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
    cv2.imshow("Frame", frame)



    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break




cv2.destroyAllWindows()
vs.stop()

