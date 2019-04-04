from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    rnn = torch.load("model/test.pt")

    hidden = rnn.init_hidden(1)
    output = rnn.init_input(1)
    outputs = []
    regularize = torch.nn.Sigmoid()
    for _ in range(10):
        output, hidden = rnn(output, hidden)
        outputs.append(output)
    print(outputs)

if __name__ == "__main__":
    main()
