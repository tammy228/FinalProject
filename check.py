import os
import shutil
from os.path import join
from testModel import recognizeFace
from keras.models import load_model
#from facedetect_dlib import findface_dlib_forTakingPic
from facedetect_openCV import findface_openCV_forTakingPic
from time import sleep

dir_name = 'picture'
data_path = '/home/pi/FinalProject/' + dir_name
model = load_model('/home/pi/FinalProject/testGroupFace.h5')

while True:
	if(os.listdir(data_path)):
		sleep(1)
		pic_name = os.listdir(data_path)
		for i in pic_name :	
			fullpath = join(data_path,i)
			findface_openCV_forTakingPic(dir_name,fullpath, i)
		
		for i in pic_name :	
			fullpath = join(data_path,i)
			name = recognizeFace(fullpath,model)
			print("This person is: %s" %(name))
			shutil.move(fullpath,"/home/pi/FinalProject/moved_picture")
