import time
from picamera.array import PiRGBArray
import datetime
import cv2
import json

text = None # global variable: vision status
quantum = 0 # global variable: control save imgShot frequency
lock = 0 # global variable: control save imgShot
key = None # global variable: control loop

conf = json.load(open("conf.json"))
# prepare haarcascade classifier
haarcascadeFile = "haarcascade_frontalface_" + conf["haarcascadeVersion"] + ".xml"
face_cascade = cv2.CascadeClassifier("haarcascades/" + haarcascadeFile)

def init_cam(camera):
        camera.resolution = tuple(conf["resolution"])
        camera.framerate = conf["fps"]
        time.sleep(conf["camera_warmup_time"])

def processing_frame(camera):
    rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))

    for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame = f.array # grab the raw NumPy array representing the image and initialize

        
        global text
        text = "Streaming"

        frame = find_face_cv2(frame) # loop for finding faces
        
        frame = update_vision_status(frame)
        
        yield frame
        
        if conf["show_video"]:
        
            cv2.imshow("Security Feed", frame)

            key = cv2.waitKey(1) & 0xFF

            # if the `q` key is pressed, break from the lop
            if key == ord("q"):
                break
        
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

def find_face_cv2(frame):
    face_rects = face_cascade.detectMultiScale(frame, 1.3, 5)
    global quantum
    global lock
    if quantum == 0:
        lock = 0
    if lock == 1:
        quantum -= 1
    # loop for finding faces
    cnt = 1
    for (x, y, w, h) in face_rects:
        global text
        text = "Streaming: person in camera vision"
        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        if lock == 0:
            save_imgShot(frame[y1:y2, x1:x2],cnt)
            cnt += 1

    if lock == 0:
        lock = 1
        quantum = conf["min_save_seconds"]
    return frame

def update_vision_status(frame):
    timestamp = datetime.datetime.now()
    cv2.putText(frame, "Pi vision: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    return frame



def save_imgShot(imgShot,cnt):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    try:
        imgShotpath = "/home/pi/FinalProject/second_picture/"
        imgShotname = "num_" + str(cnt) + "_" + timestr + ".jpg"
        cv2.imwrite(imgShotpath + imgShotname, imgShot)
    except:
        print("can't save imgShot")