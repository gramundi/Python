# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data =load_iris()
features=data['data']
feature_names=data['feature_names']

target = data['target']

target_names = data['target_names']

#build up the labels array converting index in names so we have the sample with names
labels = target_names[target] 

#print labels


#get the second column 
plength= features[:,2]
is_setosa = (labels == 'setosa')

#max_setosa = plength[is_setosa].max()
#min_non_setosa = plength[~is_setosa].min()

#print('Maximum of setosa:{0}.'.format(max_setosa))
#print('Minimum of others:{0}.'.format(min_non_setosa))


#classes = np.array(['uno','due','tre'])
#data1= np.array ([0,0,0])

#dataclass = classes[data1]
#print dataclass


features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')
best_acc = -1.0
for fi in xrange(features.shape[1]):
    thresh = features[:,fi].copy()
    thresh.sort()
    for t in thresh:
        pred =(features[:,fi] > t)
        acc = (pred == virginica).mean()
        if acc > best_acc:
            best_acc =acc
            best_fi =fi
            best_t=t