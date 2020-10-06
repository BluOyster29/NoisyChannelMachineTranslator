import torch

class embedding(Net):
    
    def __init__(self, vectors):
        self.vectors = vectors
        
    def embed(self, x):
        
        return torch.Tensor([self.vector[i] for i in x])