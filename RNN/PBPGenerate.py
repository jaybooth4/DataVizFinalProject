from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    rnn = torch.load("model/test.pt")

    hidden = rnn.init_hidden(1)
    output = torch.tensor([[0,0]], dtype=torch.float)
    outputs = []
    for _ in range(10):
        output, hidden = rnn(output.view(1, 1, 2), hidden)
        outputs.append(output)
    print(list(map(lambda event: (float(event[0][0][0]) * 1128, float(event[0][0][1]) * 600), outputs)))

if __name__ == "__main__":
    main()
