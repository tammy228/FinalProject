import os
import shutil
from os.path import join
from testModel import recognizeFace
from facedetect_dlib import findface_dlib_forTakingPic

data_path = '/home/pi/FinalProject/picture'

while os.listdir(data_path):
	pic_name = os.listdir(data_path)
	for i in pic_name :	
		fullpath = join(data_path,i)
		name = findface_dlib_forTakingPic(fullpath, i)
	'''
	for i in pic_name :	
		fullpath = join(data_path,i)
		name = recognizeFace(fullpath)
		print("This person is: %s" %(name))
		shutil.move(fullpath,"/home/pi/FinalProject/moved_picture")
	'''
