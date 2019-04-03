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
        self.rnn = nn.RNN(input_size=inputSize, hidden_size=hiddenSize, num_layers=numLayers, batch_first=batchFirst)
        self.loss = torch.nn.L1Loss()

    def forward(self, inputData, hidden):
        output, hidden = self.rnn(inputData, hidden)
        return output, hidden

    def init_hidden(self, batch_size):
        return Variable(torch.zeros(self.numLayers, batch_size, self.hiddenSize, dtype=torch.float))

    def cost(self, output, labels):
        return self.loss(output, labels)