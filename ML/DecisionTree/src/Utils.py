# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import numpy as np

#routine takes an array as input and returns a dictionary that maps each unique value to its indices
#Example for [1,1,2,3,3,3] return { 1:array[0,1],2:array[2],3:array[3,4,5] }
def partition(a):
    return {c: (a==c).nonzero()[0] for c in np.unique(a)}

#H = -sum pi*log(pi) where pi is the freq of the pi values of the s property
def entropy(s):
    res = 0
    val, counts = np.unique(s, return_counts=True)
    freqs = counts.astype('float')/len(s)
    for p in freqs:
        if p != 0.0:
            res -= p * np.log2(p)
    return res

def mutual_information(y, x):

    res = entropy(y)

    # We partition x, according to attribute values x_i
    val, counts = np.unique(x, return_counts=True)
    freqs = counts.astype('float')/len(x)

    # We calculate a weighted average of the entropy
    for p, v in zip(freqs, val):
        res -= p * entropy(y[x == v])

    return res

#if the array contain just one value is pure remember a box a green ball is pure entropy==0
def is_pure(s):
    return len(set(s)) == 1

def recursive_split(x, y):
    # If there could be no split, just return the original set
    if is_pure(y) or len(y) == 0:
        return y

    # We get attribute that gives the highest mutual information
    gain = np.array([mutual_information(y, x_attr) for x_attr in x.T])
    print "GAIN"
    
    print gain
    #argmax function give us back the index of the array max value
    selected_attr = np.argmax(gain)
    
    print "selected Attribute"
    print selected_attr 

    # If there's no gain at all, nothing has to be done, just return the original set
    if np.all(gain < 1e-6):
        return y


    # We split using the selected attribute Remeber x in a Mat[n,m] and x[:,y] return the y column of the matrix
    sets = partition(x[:, selected_attr])

    res = {}
    for k, v in sets.items():
        y_subset = y.take(v, axis=0)
        x_subset = x.take(v, axis=0)
        print k,v
        print y_subset
        res["x_%d = %d" % (selected_attr, k)] = recursive_split(x_subset, y_subset)

    return res