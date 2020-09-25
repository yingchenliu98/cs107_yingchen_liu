#!/usr/bin/env python3

# Coder: Victor Avram
# Listener: John Alling
# Sharer: Yingchen Liu
    
# AC207 - Paired Programming 4 Exercise 1
import numpy as np
# Define an outer function that creates the layer and accepts the number of inputs, the number of 
def create_layer(shape,actv):
    
    # Define a nested function that accepts inputs, weights, and bias and returns the layer output
    def produce_output(inputs,weights,bias):
        # Assert inputs, weights, and bias are the correct size
        assert shape[0] == len(inputs)
        assert shape[1] == len(weights[0])
        assert shape[1] == len(bias)
    
        # Compute the weighted sum of the inputs for each node (plus the bias term)
        input_list = np.dot(inputs,weights) + bias
        
        # Compute the output from the layer
        output = actv(input_list)

        return output

    return produce_output

# Generate initial layer inputs
t = np.random.uniform(0.0, 1.0, 4).reshape(1,-1)[0] # input to the network

# Define the number of inputs and units
shape1 = [np.size(t), 3]
shape2 = [3, 1]

# Initialize weights and biases
w1 = [[1,2,1], [1,1,1], [3,2,1], [1,1,1]]
w2 = [[1],[2],[5]]
b1 = [0, 1, 2]
b2 = [-2]

# Initialize the layers
layer1 = create_layer(shape1,np.tanh)
layer2 = create_layer(shape2,np.tanh)

# Run through the network
h1 = layer1(t, w1, b1) # First layer # [[0.99893778 0.99981137 0.99990433]]
print(h1)
h2 = layer2(h1, w2, b2) # Last layer # [[0.99483093 0.99998659 0.99926828 1.        ]]
print(h2)