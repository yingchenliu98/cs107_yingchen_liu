# Pair programming 5

# coder: Kaiwen Li
# sharer: Yingchen Liu

from random import random
import numpy as np

class Layer():
    def __init__(self, shape, actv):
        self.actv = actv
        self.weights = np.random.rand(shape[0], shape[1])
        self.biases = np.random.rand(shape[1])
    
    def __str__(self):
        str_note = "Actv func: " + str(self.actv) + "\n" + "Weights: " + str(self.weights) + "\n" + "Biases: " + str(self.biases)
        return str_note
    
    def __repr__(self):
        class_name = type(self).__name__
        return "%s(actv=%r, weights=%r, biases=%r)" % (class_name, self.actv, self.weights, self.biases)

    def __eq__(self, other):
        return (self.actv == other.actv)

    def forward(self, inputs):
        # Compute the weighted sum of the inputs for each node (plus the bias term)
        input_list = np.dot(inputs, self.weights) + self.biases

        output = self.actv(input_list)

        return output
        
# demo
shape1 = [4, 4]
shape2 = [4, 1]

actv1 = np.tanh
actv2 = np.sinh
t = np.random.uniform(0.0, 1.0, 4).reshape(1,-1)[0]
layer1 = Layer(shape1, actv1)
h1 = layer1.forward(t) 
print(h1.shape)

layer2 = Layer(shape2, actv2)
h2 = layer2.forward(h1)
print(h2)



# demo dunders
print(str(layer1))
print(repr(layer1))
print(layer1 == layer2)