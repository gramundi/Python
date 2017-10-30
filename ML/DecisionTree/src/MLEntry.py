# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import Utils as utls
from pprint import pprint

if __name__ == "__main__":
    print "Hello World"

import numpy as np
x1 = [0, 1, 1, 2, 2, 2]
x2 = [0, 0, 1, 1, 1, 0]
y = np.array([0, 0, 0, 1, 1, 0])

#print partition(x1)

#Implement the Trasponse of a matrix 
X = np.array([x1, x2]).T
#print set (x1)
#print utls.is_pure(x1)


t = [-3,-4,-1,-1,-5]
print 1e-6
if np.all(t > 0):
        print "fabio"

#print X.T


#pprint(utls.recursive_split(X, y))
