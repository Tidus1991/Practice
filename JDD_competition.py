# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:29:18 2017

@author: Tidus
"""

import matplotlib.pyplot as plt
from scipy import interp
from sklearn.metrics import roc_curve, auc
from sklearn import svm
from sklearn.cross_validation import train_test_split,StratifiedKFold
import pandas as pd
from collections import Counter
import time
import numpy as np
start = time.time()
from sklearn import preprocessing

t_login = pd.read_csv('t_login.csv')
t_trade = pd.read_csv('after_trade.csv')
login = pd.DataFrame(t_login.values)
trade = pd.DataFrame(t_trade.values)
import sklearn

#----------------------------------------------------#
                    # data clean

#time transfor
#for i in range(len(trade)):
#    trade[1][i] = int(trade[1][i][:2]) * 60 + int(trade[1][i][3:5])

# risk record
risk = {}
j = 0
count_trade = Counter(trade[0])

for i in trade[0]:
    risk[i] = risk.get(i, 0) + trade[2][j]
    j += 1
# avg risk
for i in set(trade[0]):
    risk[i] = risk[i] / count_trade[i]


#multiple situation counter
# c = 0
# for i in set(trade[0]):
#    if risk[i] != 0 and risk[i] != 1:
#        c += 1

#del nonactive users
count_login = Counter(login[0])

diff_login = set(login[0]) - set(risk)
login_stcount = 0
for index, id in enumerate(login[0]):
    if id in diff_login:
        repeat = count_login[id]
        login = login.drop(index)
        login_stcount += 1
        if count_login == repeat:
            diff_login.remove(id)
            login_stcount = 0
        print('(login)No.%d data is delete'%id)

diff_trade = set(risk) - set(login[0])
trade_stcount = 0
for index, id in enumerate(trade[0]):
    if id in diff_trade:
        repeat = count_trade[id]
        trade = trade.drop(index)
        trade_stcount += 1
        if diff_trade == repeat:
            diff_trade.remove(id)
            trade_stcount = 0
        print('(trade)No.%d data is delete' % id)

# add risk
# login_risk = []
# for i in login[0]:
#     login_risk.append(risk[i])
# login.insert(9, '9', login_risk)

# add label
# label = []
# for i in login[0]:
#     if risk[i] != 0:
#         label.append(1)
#     else:
#         label.append(0)








#----------------------------------------------------#
           # data transformal and normalization

#f_change
# start_index = 0
# stop_index = 0
# for i in range(0,len(login)):
#     try:
#         if login[0][i] == login[0][i+1]:
#             stop_index += 1
#         else:
#             ratio = ((len(set(login[2][start_index:stop_index+1])))/(stop_index-start_index+1))\
#                             -(len(set(login[2][start_index:stop_index + 1])))
#             for i in range(start_index, stop_index+1):
#                 login[8][i] = (round(ratio, 2))
#             print('Series:',round(ratio, 2))
#             stop_index = i + 1
#             start_index = stop_index
#     except:
#         if stop_index == start_index:
#             login[8][start_index] = 0
#             print('End:',round(ratio, 2))
#         ratio = (len(set(login[2][start_index:stop_index + 1]))) / (stop_index - start_index+1)\
#                       -(len(set(login[2][start_index:stop_index + 1])))
#         for i in range(start_index, stop_index+1):
#             login[8][i] = (round(ratio, 2))
#         print('End:',round(ratio, 2))
#
# end = time.time()
# print('waste time:',round(end - start, 2),'second')


start = time.time()

# cv
start_index = 0
stop_index = 0
for i in range(0,len(login)):
    try:
        if login[0][i] == login[0][i+1]:
            stop_index += 1
        else:
            cv = np.std(login[6][start_index:stop_index + 1]) / np.mean(login[6][start_index:stop_index + 1])
            for j in range(start_index, stop_index+1):
                login[14][j] = (round(cv, 4))
            print('cv_loop 1','Series:',round(cv, 4))
            stop_index = i + 1
            start_index = stop_index
    except:
        if stop_index == start_index:
            login[14][start_index] = 0
            print('cv_loop 1','SigEnd:',round(0, 4))
            break
        cv = np.std(login[6][start_index:stop_index + 1]) /  np.mean(login[6][start_index:stop_index + 1])
        for j in range(start_index, stop_index+1):
            login[14][j] = (round(cv, 4))
        print('cv_loop 1','SeqEnd:',round(cv, 4))

# ratio
for loop in range(5):
    start_index = 0
    stop_index = 0
    for i in range(0,len(login)):
        try:
            if login[0][i] == login[0][i+1]:
                stop_index += 1
            else:
                ratio = (len(set(login[1+loop][start_index:stop_index + 1]))) / (stop_index - start_index+1)
                for j in range(start_index, stop_index+1):
                    login[9+loop][j] = (round(ratio, 4))
                print('ratio_loop %d'%(loop+1),'Series:',round(ratio, 4))
                stop_index = i + 1
                start_index = stop_index
        except:
            if stop_index == start_index:
                login[9+loop][start_index] = 0
                print('ratio_loop %d'%(loop+1),'SigEnd:',round(0, 4))
                break
            ratio = (len(set(login[1+loop][start_index:stop_index + 1]))) / (stop_index - start_index + 1)
            for j in range(start_index, stop_index+1):
                login[9+loop][j] = (round(ratio, 4))
            print('ratio_loop %d'%(loop+1),'SeqEnd:',round(ratio, 4))




end = time.time()
print('--------------------\nwaste time:', round(end - start, 2),\
          'second, calculation complished\n--------------------' )


#normalization
# for i in range(1,7):
#     login[i] = sklearn.preprocessing.scale(login[i])

#----------------------------------------------------#
                     # SVM ML


# string = []
# for i in range(1,9):
#     for j in range(len(X)):
#         if isinstance(X[i][j],str):
#             string.append([i,j])
#         print('now step:',i,j)
#
# if string != []:
#     print('notgood')
#     for t in range(string[0][1],string[-1][1]):
#         X[5][j] = float([X[5][t]])
#         print('replace:',j)


# Test_score = 0
# Train_socre = 0
# X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.75)
# lr = svm.SVC(kernel='linear', probability=True)
# lr.fit(X_train,y_train)
# Test_score = Test_score + lr.score(X_test,y_test)
# Train_socre = Train_socre + lr.score(X_train,y_train)
#
#
# mean_tpr = 0.0
# mean_fpr = np.linspace(0, 1, 100)
# all_tpr = []
# cv = StratifiedKFold(y, n_folds=5)
#
# for i, (train, test) in enumerate(cv):
#     #通过训练数据，使用svm线性核建立模型，并对测试集进行测试，求出预测得分
#     probas_ = lr.fit(X_train, y_train).predict_proba(X_test)
# #    print set(y[train])                     #set([0,1]) 即label有两个类别
# #    print len(X[train]),len(X[test])        #训练集有84个，测试集有16个
# #    print "++",probas_                      #predict_proba()函数输出的是测试集在lael各类别上的置信度，
# #    #在哪个类别上的置信度高，则分为哪类
#     # Compute ROC curve and area the curve
#     #通过roc_curve()函数，求出fpr和tpr，以及阈值
#     fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1])
#     mean_tpr += interp(mean_fpr, fpr, tpr)          #对mean_tpr在mean_fpr处进行插值，通过scipy包调用interp()函数
#     mean_tpr[0] = 0.0                               #初始处为0
#     roc_auc = auc(fpr, tpr)
#     #画图，只需要plt.plot(fpr,tpr),变量roc_auc只是记录auc的值，通过auc()函数能计算出来
#     plt.plot(fpr, tpr, lw=1, label='ROC fold %d (area = %0.2f)' % (i+1, roc_auc))
#
# #画对角线
# plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')
#
# mean_tpr /= len(cv)                     #在mean_fpr100个点，每个点处插值插值多次取平均
# mean_tpr[-1] = 1.0                      #坐标最后一个点为（1,1）
# mean_auc = auc(mean_fpr, mean_tpr)      #计算平均AUC值
# #画平均ROC曲线
# #print mean_fpr,len(mean_fpr)
# #print mean_tpr
# plt.plot(mean_fpr, mean_tpr, 'k--',
#          label='Mean ROC (area = %0.2f)' % mean_auc, lw=2)
#
# plt.xlim([-0.05, 1.05])
# plt.ylim([-0.05, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()
