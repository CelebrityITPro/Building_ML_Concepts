# Assume 3 inputs from 3 previous neurons

inputs = [1, 2, 3]  # Inputs from previous neurons
weights = [0.2, 0.8, -0.5]  # Weights for each input
bias = 2  # Bias term

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)  # Output of the neuron