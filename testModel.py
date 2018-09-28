import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.preprocessing.image import load_img ,img_to_array
from testModelFun import read_name_list
from time import time

def recognizeFace(path,model):
	img = load_img(path,target_size=(150,150))
	x = img_to_array(img)
	x = np.expand_dims(x, axis=0)
	#x = preprocess_input(x)
	x = x.astype('float32')
	x = x/255.0

	prob = model.predict(x)
	max_index = np.argmax(prob)
	name_list = read_name_list('/home/pi/FinalProject/data/test')
	if prob[0][max_index] > 0.5:
	    show_name = name_list[max_index]
	else:
	    show_name = 'Can Not Identify'
	return show_name
