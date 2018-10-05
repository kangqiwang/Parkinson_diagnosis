# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:12:19 2018

@author: Administrator
"""

import numpy as np
from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
"""
'from neupy.algorithms import PNN
"""

dataset = datasets.load_iris()
data, target = dataset.data, dataset.target

print("> Start classify iris dataset")
skfold = StratifiedKFold(n_splits=10)

for i, (train, test) in enumerate(skfold.split(data, target), start=1):
    x_train, x_test = data[train], data[test]
    y_train, y_test = target[train], target[test]
    print(x_train)
    