import os
import numpy as np

def read_name_list(path):
	name_list = []
	result = os.listdir(path)
	result.sort()
	for child_dir in result:
		name_list.append(child_dir)
	
	return name_list
