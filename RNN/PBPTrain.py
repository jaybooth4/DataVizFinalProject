from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

def main():
    playData = PBPDataset('../data/pattern.csv')

    rnn = PBPModel(2, 2, numLayers=3)

    optimizer = torch.optim.Adam(rnn.parameters(), lr=.1)

    for epoch in range(40):
        for batch, labels in playData:

            hidden, loss = rnn.init_hidden(1), 0
            for inputPoint, label in zip(batch[0], labels[0]):
                output, hidden = rnn(inputPoint.view(1, 1, 2), hidden)
                # print("Point")
                # print(inputPoint)
                # print(label)
                # print(output)
                # print(hidden)
                loss += rnn.cost(output, label)

            print(loss)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    torch.save(rnn, "model/test.pt")

if __name__ == "__main__":
    main()
