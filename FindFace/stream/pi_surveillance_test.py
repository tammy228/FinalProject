# import the necessary packages
from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import datetime
import dropbox
import imutils
import json
import time
import cv2
 

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
	help="path to the JSON configuration file")
args = vars(ap.parse_args())
 
# filter warnings, load the configuration and initialize the Dropbox
# client
warnings.filterwarnings("ignore")
conf = json.load(open(args["conf"]))
client = None

# prepare haarcascade classifier
#haarcascadeVersion = "alt"
haarcascadeFile = "haarcascade_frontalface_" + conf["haarcascadeVersion"] +".xml"
face_cascade = cv2.CascadeClassifier("haarcascades/"+haarcascadeFile)



# check to see if the Dropbox should be used

if conf["use_dropbox"]:

	# connect to dropbox and start the session authorization process

	client = dropbox.Dropbox(conf["dropbox_access_token"])

	print("[SUCCESS] dropbox account linked")

# initialize the camera and grab a reference to the raw camera capture

try:
	camera = PiCamera()
	
	camera.resolution = tuple(conf["resolution"])
	
	camera.framerate = conf["fps"]
	
	rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))

	# allow the camera to warmup, then initialize the average frame, last

	# uploaded timestamp, and frame motion counter

	print("[INFO] warming up...")

	time.sleep(conf["camera_warmup_time"])

	avg = None

	lastUploaded = datetime.datetime.now()

	# add time to reduce times of taking pictures 
	quantum = 0
	lock = 0

	motionCounter = 0
	# capture frames from the camera
	
	for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		# grab the raw NumPy array representing the image and initialize
	
		# the timestamp and occupied/unoccupied text
	
		frame = f.array
                #print("frame")
                #print(frame)
	
		timestamp = datetime.datetime.now()
	
		text = "There are not any person"
	
	 
	
		# resize the frame, convert it to grayscale, and blur it
	
		frame = imutils.resize(frame, width=500)
	
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
		##gray = cv2.GaussianBlur(gray_frame, (21, 21), 0)
	        face_rects = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

	 
	
		# if the average frame is None, initialize it
	
		if avg is None:
	
			print("[INFO] starting background model...")
	
			avg = gray_frame.copy().astype("float")
	
			rawCapture.truncate(0)
	
			continue
		if quantum == 0:
			lock = 0

		if lock == 1:
			quantum -= 1
		
		
	        # loop for finding faces
                cnt = 1
                for(x, y, w, h) in face_rects:
                    x1 = x
                    y1 = y
                    x2 = x + w
                    y2 = y + h

                    imgShot = gray_frame[y1:y2, x1:x2]
		    print("imgShot")
		    print(imgShot)
                    cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 0, 0), 2)
                    timestr = time.strftime("%Y%m%d-%H%M%S")
                    if lock == 0:
	                time.sleep(1)
			try:
                            imgShotpath = "/home/pi/FinalProject/second_picture/"
	                    imgShotname = "num_" + str(cnt) + "_" + timestr + ".jpg"
	                    cv2.imwrite(imgShotpath + imgShotname , imgShot)
	                except:
                            print("can't save imgShot")

                    text = "person in camera vision"
                if lock == 0:
			lock = 1
			quantum = 5    

		# draw the text and timestamp on the frame
	
		ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
	
		cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
	
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	
		cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
	
			0.35, (0, 0, 255), 1)
	
		# check to see if the room is occupied
		if text == "person in camera vision":
			# check to see if enough time has passed between uploads
	
			if (timestamp - lastUploaded).seconds >= conf["min_upload_seconds"]:
	
				# increment the motion counter
	
				motionCounter += 1
	
	 
	
				# check to see if the number of frames with consistent motion is
	
				# high enough
	
				if motionCounter >= conf["min_motion_frames"]:
	
					# check to see if dropbox sohuld be used
	
					if conf["use_dropbox"]:
	
						# write the image to temporary file
	
						t = TempImage()
	
						cv2.imwrite(t.path, frame)
	
	 
	
						# upload the image to Dropbox and cleanup the tempory image
	
						print("[UPLOAD] {}".format(ts))
	
						path = "/{base_path}/{timestamp}.jpg".format(
	
						    base_path=conf["dropbox_base_path"], timestamp=ts)
	
						client.files_upload(open(t.path, "rb").read(), path)
	
						t.cleanup()
	
	 
	
					# update the last uploaded timestamp and reset the motion
	
					# counter
	
					lastUploaded = timestamp
	
					motionCounter = 0
	
	 
	
		# otherwise, the room is not occupied
	
		else:
	
			motionCounter = 0
	
		# check to see if the frames should be displayed to screen
	
		if conf["show_video"]:
	
			# display the security feed
	
			cv2.imshow("Security Feed", frame)
	
			key = cv2.waitKey(1) & 0xFF
	
	 
	
			# if the `q` key is pressed, break from the lop
	
			if key == ord("q"):
	
				break
	
	 
	
		# clear the stream in preparation for the next frame
	
		rawCapture.truncate(0)
except KeyboardInterrupt:
	camera.close()
except:
	camera.close()
        print("something wrong")
finally:
	camera.close()
