#!/usr/bin/env python3

""" Exercise #1: logistic regression in two dimensions.
                 skeleton code.
"""

import numpy as np
import torch
import torch.nn.functional as F

## load the 2d data (x_data), with the labels (y_data).
## the labels are {0,1}.
x_data, y_data = torch.load ( "01_logit.p" )

## now define your neural network.
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        ...
        
    def forward(self, x):
        ## the forward pass must consist of a 
        ## sigmoidal function (F.sigmoid), applied to 
        ## a linear layer ( torch.nn.Linear ), that takes
        ## x as its input.
        y_pred =  ...
        return y_pred
    
# Instantiate the model
model = Model()

## define your loss function (e.g. torch.nn.BCELoss)
criterion = ...

## choose an optimizer (torch.optim.Adam, torch.optim.SGD, ... )
## it takes model.parameters() as input. Choose a learning rate.
optimizer = ...

# Training loop
for epoch in range(1000):
    # Forward pass: Compute predicted y by passing x_data to the model
    y_pred = model(x_data)
    
    # Compute and print loss
    loss = criterion(y_pred, y_data)
    print ( epoch, loss.data[0] )
    
    # Reset gradient, perform a backward pass, and update the weights.
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

## print the result
for f in model.parameters():
    print('data is')
    print(f.data)
    print(f.grad)

## obtain the learned weights
w = list(model.parameters())
w0 = w[0].data.numpy()
w1 = w[1].data.numpy()

import matplotlib.pyplot as plt

print ( "Final gradient descent, adam:", w )

## plot the data and decision boundary
plt.scatter(x_data[:,0], x_data[:,1], c=y_data.reshape(100), s=100, alpha=0.5)
x_axis = np.linspace(-6, 6, 100)
y_axis = -(w1[0] + x_axis*w0[0][0]) / w0[0][1]
line_up, = plt.plot(x_axis, y_axis,'r--', label='decision boundary')
plt.legend(handles=[line_up])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
#plt.show()
plt.savefig ( "01_logit.png" )
