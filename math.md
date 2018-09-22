标准化

	from sklearn import preprocessing
	import numpy as np
	X_train = np.array([[ 1., -1.,  2.],
	                     [ 2.,  0.,  0.],
	                     [ 0.,  1., -1.]])
	X_scaled = preprocessing.scale(X_train)

	X_scaled                                          
	array([[ 0.  ..., -1.22...,  1.33...],
       [ 1.22...,  0.  ..., -0.26...],
       [-1.22...,  1.22..., -1.06...]])


均值大于中位数 right skew
反之

差得远，有偏分布， 有离群分布。 解决： log 数据 可以将近正太。

箱型图可以看出数据是否有偏
 

正太分布 ： 波动大，方差大， 矮胖
方差小，波动小，高瘦


归一化


生成多项式特征
X 的特征已经从 (X_1, X_2) 转换为 (1, X_1, X_2, X_1^2, X_1X_2, X_2^2) 。

