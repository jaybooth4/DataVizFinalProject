from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    # Read in data
    playData = PBPDataset('../data/pbp_final_small.csv')

    rnn = PBPModel(2, 2)

    optimizer = torch.optim.Adam(rnn.parameters(), lr=0.1)

    print(rnn)
    
    for batch, labels in playData:

        initHidden = rnn.init_hidden(1)

        output, _ = rnn(batch, initHidden)

        print(output.size())
        print(output.type())
        print(labels.size())
        print(labels.type())

        loss = rnn.cost(output, labels)
        
        print("loss")
        print(loss)
        loss.backward()
        optimizer.step()

if __name__ == "__main__":
    main()
