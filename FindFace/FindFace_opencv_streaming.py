import io
from time import sleep
import picamera
import cv2
import numpy as np

#Create a memory stream so photos doesn't need to be saved in a file
stream = io.BytesIO() #variableA

#Get the picture (low resolution, so it should be quite fast)
#Here you can also specify other parameters(e.g. rotate the image)

with picamera.PiCamera() as camera:
	camera.resolution = (320, 240) #can change whenever you need

	camera.start_preview()
	#camera warm-up time
	sleep(2)

	#need to set format because [BytesIO] object no filename
	camera.capture(stream, format = 'jpeg') #(variableA, savedfile's format)

#Convert the picture into a numpy array
#Load the motion data from the string to a numpy array
buff = np.fromstring(stream.getvalue(), dtype=np.uint8) #dtype can design by yourself. uint8 is Unsigned integer(0 to 255)

#Now creates an OpenCV image
img = cv2.imdecode(buff, 1) #image deocde. (input arrray, some said: image's color scheme)

#Load a cascade file for detecting faces
haarObject = "frontalface"
haarVersion = "default" #default, alt, alt2, alt_tree
face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_" + haarObject + "_" + haarVersion + ".xml")

#Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Look for faces in the gray Image using the loaded cascade file
face_rects = face_cascade.detectMultiScale(gray_img,1.1,5) #probably (image, scaleFacotr, minNeighbors)

print "Found" + str(len(face_rects)) + "face(s)"

#Draw a rectangle around every found face
for(x,y,w,h) in face_rects:
	x1=x
	y1=y
	x2=x+w
	y2=y+h
	cv2.rectangle(img, (x1,y1),(x2,y2), (255,193,193),2) # (image, , , revtangle's color, thickness of rectangle's line)
	grayShot = gray_img[y1:y2, x1:x2] #to save rectangle's region

#Save the result image
cv2.imwrite('test.jpg', img)
