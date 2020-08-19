import numpy as np

"""

    Base Class for MachineZero
    
    Needed Objects
        # Input
        # Weights
        # Bias 
        
    Needed Modules
        # Numpy

"""

np.random.seed(0)

inputs = [3.0, 4.2, 5.1, 0.2]
weights = [3.2, 4.4, 1.0, 2.3, 0.8]


class Object:

    def __init__(self, n_inputs, n_nureons):
        self.Weights = 0.10 * np.random.randn(n_inputs, n_nureons)
        self.Bias = 0.10 * np.zeros((1, n_nureons))

    def construction(self, inputs):
        self.output = np.dot(inputs, self.Weights) + self.Bias

Layer1 = Object(4,5)
Layer2 = Object(5,2)

Layer1.construction(inputs)
print(Layer1.output)

Layer2.construction(Layer1.output)
print(Layer2.output)