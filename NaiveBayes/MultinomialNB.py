# -*- coding: utf-8 -*-
"""
Created on 2017/11/24 13:43

@author: Tidus
"""

from NaiveBayes_Basic import *

class MultinomialNB(NaiveBayes):
	def feed_data(self, x, y, sample_weight=None):
		if isinstance(x, list):
			features = map(list, zip(*x))
		else:
			features = x.T
		features = [set(feat) for feat in features]
		feat_dics = [{_l:i for i, _l in enumerate(feats)} for feats in features]
		label_dic = {_l:i for i, _l in enumerate(set(y))}
		x = np.array([[feat_dics[i][_l] for i,_l in enumerate(sample)]for sample in x])
		y = np.array([label_dic[yy] for yy in y])
		cat_counter = np.bincount(y)
		n_possibilities = [len(feats) for feats in features]
		labels = [y == value for value in range(len(cat_counter))]
		labelled_x = [x[ci].T for ci in labels]
		self._x, self._y = x, y
		self._labelled_x, self._labelled_zip = labelled_x, list(zip(labels, labelled_x))
		(self._cat_counter, self._feat_dics, self._n_possibilities) = \
		(cat_counter, feat_dics, n_possibilities)

		self.label_dic = {i:_l for _l, i in label_dic.items()}
		self.feed_sample_weight(sample_weight)

	def feed_sample_weight(self, sample_weight=None):
		self._con_counter = []
		for dim, _p in enumerate(self._n_possibilities):
			if sample_weight is None:
				self._con_counter.append([np.bincount(xx[dim], minlength=_p)
				                          for xx in self._labelled_x])
			else:
				self._con_counter.append([
					np.bincount(xx[dim], weights=sample_weight[label] / sample_weight[label].mean(),
					            minlength = _p) for label, xx in self._labelled_zip])

	def _fit(self, lb):
		n__dim = len(self._n_possibilities)
		n_category = len(self._cat_counter)
		p_category = self.get_prior_probability(lb)
		data = [None] * n__dim
		for dim, n_possibilities in enumerate(self._n_possibilities):
			data[dim] = [[(self._con_counter[dim][c][p] + lb) / (self._cat_counter[c] + lb *n_possibilities)
			              for p in range(n_possibilities)] for c in range(n_category)]
		self._data = [np.array(dim_info) for dim_info in data]

		def func(input_x, tar_category):
			rs =1
			for d, xx in enumerate(input_x):
				rs *= data[d][tar_category][xx]
			return rs * p_category[tar_category]
		return func

	def _transfer_x(self, x):
		for j, char in enumerate(x):
			x[j] = self._feat_dics[j][char]
		return x
	
	def visualize(self):
		import matplotlib.pyplot as plt
		from pylab import mpl
		mpl.rcParams['font.sans-serif'] = ['FangSong']
		mpl.rcParams['axes.unicode_minus'] = False
		data = nb['data']
		colors = {'e': 'lightSkyBlue', 'p': 'orange'}
		_rev_feat_dics = [{_val: _key for _key, _val in _feat_dic.items()} for _feat_dic in self._feat_dics]
		for _j in range(nb['x'].shape[1]):
			sj = nb['n_possibilities'][_j]
			tmp_x = np.arange(1, sj + 1)
			title = '$j = {}; S_j = {}$'.format(_j + 1, sj)
			plt.figure()
			plt.title(title)
			for _c in range(len(nb.label_dic)):
				plt.bar(tmp_x - 0.35 * _c, data[_j][_c, :], width=0.35, facecolor=colors[nb.label_dic[_c]],
				        edgecolor='white',
				        label='class: {}'.format(nb.label_dic[_c]))
			plt.xticks([i for i in range(sj + 2)], [''] + [_rev_feat_dics[i] for i in range(sj)] + [''])
			plt.ylim(0, 1.0)
			plt.legend()
			plt.savefig('d{}'.format(_j + 1))

if __name__ == '__main__':
	import time
	from Util import DataUtil
	#for dataset in ('balloon1.0', 'balloon1.5'):
	dataset = 'mushroom'
	_x, _y = DataUtil.get_dataset(dataset, 'Data/{}.txt'.format(dataset))
	learning_time = time.time()
	nb = MultinomialNB()
	nb.fit(_x, _y)
	learning_time = time.time() - learning_time
	estimation_time = time.time()
	nb.evaluate(_x, _y)
	estimation_time = time.time() - estimation_time
	print(
		'Model building : {:12.6} s\n'
		'Estimation : {:12.6} s\n'
		'Total : {:12.6} s'.format(learning_time, estimation_time, learning_time+estimation_time)
	)
	nb.visualize()
