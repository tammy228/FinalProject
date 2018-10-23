import os
import shutil
from os.path import join
from testModel import recognizeFace
from keras.models import load_model
#from facedetect_dlib import findface_dlib_forTakingPic
from facedetect_openCV import findface_openCV_forTakingPic
from time import sleep

dir_name = 'media'
processed_img_dir = 'second_picture'
data_path = '/var/www/html/' + dir_name
data_path2 = '/home/pi/FinalProject/second_picture'
model = load_model('/home/pi/FinalProject/eighteenClassmate_Model2_Bin.h5')

while True:
	if(os.listdir(data_path)):
		sleep(1)
		pic_name = os.listdir(data_path)
		for i in pic_name :	
			fullpath = join(data_path,i)
			findface_openCV_forTakingPic(dir_name,fullpath, i)
			os.remove(fullpath)
			#print(i)
			#if(os.listdir("/home/pi/FinalProject/media/")):
				#shutil.move("/home/pi/FinalProject/media/" + i,"/home/pi/FinalProject/second_picture")
	sleep(1)
	if(os.listdir(data_path2)):
		pic_name2 = os.listdir(data_path2)
		for i in pic_name2 :	
			fullpath2 = join(data_path2,i)
			name = recognizeFace(fullpath2,model)
			print("This person is: %s" %(name))
			shutil.move(fullpath2,"/home/pi/FinalProject/third_picture")
