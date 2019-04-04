from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    rnn = torch.load("model/test.pt")

    hidden = rnn.init_hidden(1)
    output = torch.tensor([[[0,0,0,0]]], dtype=torch.float)
    outputs = []
    regularize = torch.nn.Sigmoid()
    for _ in range(10):
        output, hidden = rnn(output, hidden)
        outputs.append(output)

    outputs = list(map(lambda event: (float(event[0][0][0]), float(event[0][0][1]), float(event[0][0][2]), float(regularize(event[0][0][3]))), outputs))
    print(outputs)

if __name__ == "__main__":
    main()
