import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.preprocessing.image import load_img ,img_to_array
from testModelFun import read_name_list
from time import time
import cv2

def recognizeFace(path,model):
	img_width, img_height = 150, 150
	model = load_model('/home/pi/FinalProject/eighteenPeople_model2_bin_v1.h5')
	img = load_img(path,target_size=(150,150))
	x = img_to_array(img)
	
	#img.save('test.png')
	#img.show()
	x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
	x = np.expand_dims(x, axis=0)
	x = np.expand_dims(x, axis=1)
	if x.shape == (1,1, img_width, img_height):
		x.shape = (1,img_width, img_height, 1)
	#x = preprocess_input(x)
#	x = x.astype('float32')
	x = x/255.0

	prob = model.predict(x)
	max_index = np.argmax(prob)
	name_list = read_name_list('/home/pi/FinalProject/data/test')
	print("Everyone's Probility:")
	for i in range(0, max_index+1):
		print(str(name_list[i])+":"+str(prob[0][i]))
	if prob[0][max_index] > 0.5:
	    show_name = name_list[max_index]
	else:
	    show_name = 'Can Not Identify'
	return show_name
