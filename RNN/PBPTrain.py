from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    # Read in data
    playData = PBPDataset('../data/play.csv')

    rnn = PBPModel(2, 2)

    optimizer = torch.optim.Adam(rnn.parameters(), lr=0.1)
    
    for batch, labels in playData:
        initHidden = rnn.init_hidden(batch.size[0])

        output, _ = rnn(batch, initHidden)

        loss = rnn.cost(output, labels)
        loss.backward()
        optimizer.step()

if __name__ == "__main__":
    main()
