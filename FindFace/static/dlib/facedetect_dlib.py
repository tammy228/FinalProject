import dlib
import cv2
import sys
import os, os.path
import imutils
import imageio
import numpy as np
import time

start_time = time.time()

if (len(sys.argv) < 2):
	print("Forgot directory name argument. Please try again.")
	sys.exit()

top = sys.argv[1]
OUTPUT_DIR = "Output_dlib" + "_" + sys.argv[1]

if not os.path.exists(OUTPUT_DIR):
	os.mkdir(OUTPUT_DIR)

print("img get face detector")
detector = dlib.get_frontal_face_detector()

processed_face_num = 0

for rootdir, dirs, files in os.walk(top, topdown=False):
	for dirname in dirs:
		print("    "+dirname+"=======================")
		
		OUTPUT_subdir = os.path.join(OUTPUT_DIR, dirname)
		if not os.path.exists(OUTPUT_subdir):
			os.mkdir(OUTPUT_subdir)

		abs_dirname = os.path.join(rootdir, dirname)
		files = os.listdir(abs_dirname)
		
		for filename in files:
			print("        start processing " + filename + "...")
			
			abs_filename = os.path.join(abs_dirname, filename)
			img = cv2.imread(abs_filename)

			if img is not None: # .gif can't be read by cv2.imread
				'''
				print("        {} cv2.imread failed".format(abs_filename))
				frame = imageio.mimread(abs_filename)
				print("        +++++++++")
				if frame is not None:
					tmp = np.array(frame)
					tmp = tmp[0]
					img = tmp[:,:,0:3]
				'''

				print("        img resizing...")
				img = imutils.resize(img, width=1280)

				print("        img upsampling 1 time...")
				face_rects = detector(img, 1)

				cnt = 1
				for i, d in enumerate(face_rects):
					x1 = d.left()
					y1 = d.top()
					x2 = d.right()
					y2 = d.bottom()

					imgShot = img[y1:y2, x1:x2]

					print("            img write...")
				#try:
					cv2.imwrite(OUTPUT_DIR+"/"+dirname+"/"+str(cnt)+"_"+filename, imgShot)
				#except:
					#imageio.mimsave(OUTPUT_DIR+"/"+dirname+"/"+str(cnt)+"_"+filename, imgShot)

					print("Image Shot "+dirname+" "+str(cnt)+"_"+filename+" has been processed")
					cnt+=1
					processed_face_num += 1
			print("Images " + filename + " has been processed")
		print("Images in dir " + dirname + " has been processed")

print("All images have been processed!!!")
print("{} takes --- {} seconds to --- find {} faces".format( sys.argv[0], (time.time() - start_time), processed_face_num) )
cv2.waitKey(0)
cv2.destroyAllWindows()
