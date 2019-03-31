import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from .readData import RNNDataset

torch.manual_seed(1)

# https://github.com/spro/char-rnn.pytorch

from torch.autograd import Variable

class PBPModel(nn.Module):
    def __init__(self, inputSize, hiddenSize, outputSize, numLayers=2):
        super().__init__()
        self.inputSize = inputSize
        self.hiddenSize = hiddenSize
        self.outputSize = outputSize
        self.rnn = nn.RNN(inputSize, hiddenSize, outputSize, numLayers, batch_first=True)

    def forward(self, input, hidden):
        batch_size = input.size(0)
        encoded = self.encoder(input)
        output, hidden = self.rnn(encoded.view(1, batch_size, -1), hidden)
        output = self.decoder(output.view(batch_size, -1))
        return output, hidden

    def forward2(self, input, hidden):
        encoded = self.encoder(input.view(1, -1))
        output, hidden = self.rnn(encoded.view(1, 1, -1), hidden)
        output = self.decoder(output.view(1, -1))
        return output, hidden

    def init_hidden(self, batch_size):
        if self.model == "lstm":
            return (Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)),
                    Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size)))
        return Variable(torch.zeros(self.n_layers, batch_size, self.hidden_size))



def main():
    # Define custom dataset
    playData = RNNDataset('data/play.csv')
    # Define data loader
    mn_dataset_loader = torch.utils.data.DataLoader(dataset=playData,
                                                    batch_size=2,
                                                    shuffle=False)
    
    for images, labels in mn_dataset_loader:
        # Feed the data to the model



if __name__ == "__main__":
    main()
