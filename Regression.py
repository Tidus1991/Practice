# -*- coding: utf-8 -*-
"""
Created on 2017/11/23 10:48

@author: Tidus
"""

import numpy as np
import matplotlib.pyplot as plt
x, y = [], []
for sample in open('Data/prices.txt'):
	_x, _y=sample.split(',')
	x.append(float(_x))
	y.append(float(_y))

x, y = np.array(x), np.array(y)

x = (x - x.mean()) / x.std()

plt.figure()
plt.scatter(x, y, c='g', s=6)
plt.show()

x0 = np.linspace(-2, 4, 100)
def get_model(deg):
	return lambda input_x = x0: np.polyval(np.polyfit(x, y, deg), input_x)

def get_cost(deg, input_x, input_y):
	return 0.5*((get_model(deg)(input_x)-input_y)**2).sum()

test_set = (1, 4 ,10)
for d in test_set:
	print(get_cost(d, x, y))

plt.scatter(x, y, c='g', s=20)
for d in test_set:
	plt.plot(x0, get_model(d)(), label = 'degree = {}'.format(d))

plt.xlim(-2, 4)
plt.ylim(1e5, 8e5)

plt.legend()
plt.show()
