# -*- coding: utf-8 -*-
"""
Created on 2017/11/24 11:55

@author: Tidus
"""

import numpy as np

class NaiveBayes:
	'''
	self._x,self._y 记录训练集的变量
	self._data 核心数组，存储实际使用的条件概率相关信息
	self._func 核心模型--决策函数，能够根据输入的x,y输出对应的后验概率
	self._n_possibilities 记录各个维度特征取值个数的数组
	self._labelled_x 记录按类别分开后的输入数据的数组
	self.label_zip 记录类别相关信息的数组，视具体算法，定义会有所不同
	self._cat_counter 核心数组，记录第i个数据的个数(cat是category的缩写)
	self._con_counter 核心数组，用于记录数据条件概率的原始极大似然估计
		`self._con_counter[d][c][p] = p(xd=p|y=c)(con是conditional的缩写)
	self.label_dic 核心字典，用于记录数值化类别时的转换关系
	self._feat_dics 核心字典，用于记录数值化各维度特征(feat)时的转换关系
	'''
	def __init__(self):
		self.x = self._y = None
		self._data = self._func = None
		self._n_possibilities = None
		self._labelled_x = self_label_zip = None
		self._cat_counter = self._con_counter = None
		self.label_dic = self._feat_dics = None

	def __getitem__(self, item):
		if isinstance(item, str):
			return getattr(self, '_' + item)

	def feed_data(self, x, y, sample_weight=None):
		pass

	def feed_sample_weight(self, sample_weight=None):
		pass

	def get_prior_probability(self, lb=1):
		return [(_c_num + lb) / (len(self._y) + lb *len(self._cat_counter)) for _c_num in self._cat_counter]

	def fit(self, x=None, y=None, sample_weight=None, lb=1):
		if x is not None and y is not None:
			self.feed_data(x, y, sample_weight)
		self._func = self._fit(lb)

	def _fit(self, lb):
		pass

	def predict_one(self, x, get_raw_result=False):
		if isinstance(x, np.ndarray):
			x = x.tolist()
		else:
			x = x[:]
		x = self._transfer_x(x)
		m_arg, m_probaility = 0, 0
		for i in range(len(self._cat_counter)):
			p = self._func(x, i)
			if p > m_probaility:
				m_arg, m_probaility = i, p
		if not get_raw_result:
			return self.label_dic[m_arg]
		return m_probaility

	def predict(self, x, get_raw_result=False):
		return np.array([self.predict_one(xx, get_raw_result) for xx in x])

	def evaluate(self, x, y):
		y_pred = self.predict(x)
		print('Acc: {:12.6}%'.format(100 * np.sum(y_pred == y) / len(y)))