# -*- coding: utf-8 -*-
"""
Created on 2017/11/24 16:56

@author: Tidus
"""
import numpy as np
class DataUtil:
	def get_dataset(name, path, train_num=None, tar_idx=None, shuffle=True):
		x = []
		with open(path, 'r', encoding='utf-8') as file:
			if 'balloon' or 'mushroom'in name:
				for sample in file:
					x.append(sample.strip().split(','))
		if shuffle:
			np.random.shuffle(x)
		if x[0][0] == 'p' or x[0][0] == 'e':
			tar_idx = 0
		else:
			tar_idx = -1
		y = np.array([xx.pop(tar_idx) for xx in x])
		x = np.array(x)
		if train_num is None:
			return x, y
		return (x[:train_num], y[:train_num]),(x[train_num], y[train_num])
