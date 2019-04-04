import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class PBPModel(nn.Module):
    def __init__(self, inputSize, hiddenSize, numLayers=1, dropout=0):
        super().__init__()
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.numLayers = numLayers
        self.rnn = nn.RNN(input_size=inputSize, hidden_size=hiddenSize, num_layers=numLayers, batch_first=True, nonlinearity='relu', dropout=dropout)
        self.linear = nn.Linear(hiddenSize, inputSize)
        # self.sig = torch.nn.Sigmoid()

    def forward(self, inputData, hidden):
        output, hidden = self.rnn(inputData, hidden)
        output = self.linear(output)
        return output, hidden

    def init_hidden(self, batch_size):
        return torch.zeros(self.numLayers, batch_size, self.hiddenSize, dtype=torch.float)

    # def cost(self, output, labels):
    #     return self.loss(output, labels)