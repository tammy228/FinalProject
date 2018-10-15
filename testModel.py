import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from keras.preprocessing.image import load_img ,img_to_array
from testModelFun import read_name_list
from time import time

def recognizeFace(path,model):
	img = load_img(path,target_size=(150,150))
        print("img")
        print(img)
	x = img_to_array(img)
        print("img_to_array")
        print(x)
	x = np.expand_dims(x, axis=0)
        print("expand_dims")
        print(x)
	#x = preprocess_input(x)
	x = x.astype('float32')
        print("float")
        print(x)
	x = x/255.0
        print("divide by 255")
        print(x)

	prob = model.predict(x)
	max_index = np.argmax(prob)
	name_list = read_name_list('/home/pi/FinalProject/data/test')
	if prob[0][max_index] > 0.5:
	    show_name = name_list[max_index]
	else:
	    show_name = 'Can Not Identify'
	return show_name
