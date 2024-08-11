# back propagation 

import numpy as np
import pandas as pd
import matplotlib as plt

def nlinear(x, der=False) :
    if der == True :
        return x*(1-x)
    return 1/(1+np.exp(-x))

# input
x = np.array([[0,0,1],
             [0,1,1],
             [1,0,1],
             [1,1,1]])

#output
y =np.array([[0,0,1,1]]).T
np.random.seed(1)
synapse0 = 2*np.random.random((3,1))-1
for i in range (1000) :
    layer0 = x
    layer1 = nlinear(np.dot(layer0, synapse0)) 
    layer1_error = y - layer1
    layer1_delta = layer1_error * nlinear(layer1, True)
    synapse0 += np.dot(layer0.T, layer1_delta)


print("output after trainie :", layer1)
print("actual op is : ", y)
 