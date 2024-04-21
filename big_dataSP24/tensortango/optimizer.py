"""How do we update parameters over time"""
from big_dataSP24.tensortango import mlp


class Optimizer():
    def __init__(self, neural_network: mlp.MLP, learning_rate: float = 0.01):
        self.net = neural_network
        self.lr = learning_rate

    def step(self):
        raise NotImplementedError
    

class SGD(Optimizer):
    def step(self):
        for param, grad in self.net.params_and_grads():
            param -= grad*self.lr