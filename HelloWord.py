# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:14:11 2018

@author: Administrator
"""


from sklearn import datasets

dataset=datasets.load_boston()
data, target=dataset.data, dataset.target
print('this is my dataset')
print(dataset)
