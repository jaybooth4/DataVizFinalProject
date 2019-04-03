import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.autograd import Variable

class PBPModel(nn.Module):
    def __init__(self, inputSize, hiddenSize, numLayers=1, batchFirst=True):
        super().__init__()
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.numLayers = numLayers
        self.rnn = nn.RNN(inputSize, hiddenSize, num_layers=numLayers, batch_first=batchFirst)

    def forward(self, input, hidden):
        output, hidden = self.rnn(input, hidden)
        return output, hidden

    def init_hidden(self, batch_size):
        return Variable(torch.zeros(self.numLayers, batch_size, self.hiddenSize))

    def cost(self, output, labels):
        return torch.nn.L1loss(output, labels)