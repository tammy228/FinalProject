import time
import picamera
import cv2
import os, os.path

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    start = time.time()
    camera.capture_sequence((
        '~/rawData/1/image%02d.jpg' % i
        for i in range(10)
        ), use_video_port=True)
    print('Captured 10 images at %.2ffps' % (120 / (time.time() - start)))
    camera.stop_preview()
'''
haarObject = "frontalface"
haarVersion = "default"
cascPath = "haarcascades/haarcascade_" + haarObject + "_" + haarVersion + ".xml"
face_cascade = cv2.CascadeClassifier(cascPath)

top = "rawData"
OUTPUT_DIR = "outputData"

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)

for rootdir, files in os.walk(top, topdown=False):
    for dirname in dirs:
        print(dirname+"=======================")
        OUTPUT_subdir = os.path.join(OUTPUT_DIR, dirname)
        if not os.path.exists(OUTPUT_subdir):
        os.mkdir(OUTPUT_subdir)
        
        abs_dirname = os.path.join(rootdir, dirname)
        files = os.listdir(abs_dirname)
        
        for filename in files:
            print("start processing " + filename + "...")
            abs_filename = os.path.join(abs_dirname, filename)
            img = cv2.imread(abs_filename)
            
        if frame is not None:
            img = imutils.resize(img, width=480)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_rects = faceCascade.detectMultiScale(
                gray_img,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                flags = cv2.CASCADE_SCALE_IMAGE
                )
         cnt = 1
         (x, y, w, h) in faces_rects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 10)
            x1=x
            y1=y
            x2=x+w
            y2=y+h
            grayShot = gray_img[y1:y2, x1:x2]
            
            cv2.imwrite(OUTPUT_DIR+"/"+dirname+"/"+str(cnt)+"_"+filename, imgShot)
            print("Image Shot "+dirname+" "+str(cnt)+"_"+filename+" has been processed")
            cnt+=1


print("All images have been processed!!! tab 'q'")
key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
    break


cv2.destroyAllWindows()

'''






















