import torch
from torch.nn import Sigmoid
from torch import mm

# Feed forward neural network from scratch 

class Net:
    
    def __init__(self, input_size, hidden_size, output_size):

        # input_size is the size of the vector (50 x hdden size)
        # hidden_size can be anything really I think
        # output_size is the final layer which is the size of the french vocabulary

        self.fc1 = fc(input_size, hidden_size)
        self.fc2 = fc(hidden_size, output_size)
        #self.linear = #

    def forward(self, x):
        out = self.fc1.forward(x)
        out = self.fc2.forward(out)

class fc(Net):

    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = torch.rand(input_size, output_size)
        self.bias = torch.rand(input_size)
        self.linnear = Sigmoid()

    def forward(self, x):
        x = (mm(x, self.weights) + self.bias)
        return self.linnear(x)

