import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

STARTING_OPEN_TIP = [0,601,334,0.0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]

class PBPModel(nn.Module):
    def __init__(self, inputSize, hiddenSize, numLayers=1, dropout=0):
        super().__init__()
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.numLayers = numLayers
        self.rnn = nn.RNN(input_size=inputSize, hidden_size=hiddenSize, num_layers=numLayers, batch_first=True, nonlinearity='relu', dropout=dropout)
        self.linear = nn.Linear(hiddenSize, inputSize)

    def forward(self, inputData, hidden):
        output, hidden = self.rnn(inputData, hidden)
        output = self.linear(output)
        return output, hidden

    def init_hidden(self):
        return torch.zeros(self.numLayers, 1, self.hiddenSize, dtype=torch.float)
    
    def init_input(self, batch_size=1):
        # return torch.zeros(self.numLayers, batch_size, self.inputSize, dtype=torch.float)

        return torch.tensor(STARTING_OPEN_TIP, dtype=torch.float).view(1, 1, -1)