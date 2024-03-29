import torch
from torch import nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from torch.autograd import Variable

EPOCH = 1               # train the training data n times, to save time, we just train 1 epoch

test_data=np.loadtxt('test_data.txt',dtype='float',delimiter=',')
train_data=np.loadtxt('train_data.txt',dtype='float64',delimiter=',')
x_target=train_data[:,28]
y_target=test_data[:,27]
test_data=np.delete(test_data,27,1)
train_data=np.delete(train_data,28,1)
train_data=np.delete(train_data,27,1)
train_data=np.delete(train_data,0,1)
test_data=np.delete(test_data,0,1)
test_data=torch.from_numpy(test_data)
train_data=torch.from_numpy(train_data)
x_target=torch.from_numpy(x_target).type(torch.LongTensor)
y_target=torch.from_numpy(y_target).type(torch.LongTensor)
x=torch.cat((train_data,test_data),).type(torch.FloatTensor)
y=torch.cat((x_target,y_target),).type(torch.LongTensor)
test_data=Variable(test_data, volatile=True).type(torch.FloatTensor)
train_data=Variable(train_data, volatile=True).type(torch.FloatTensor)

x, y = Variable(x), Variable(y)


print(x)