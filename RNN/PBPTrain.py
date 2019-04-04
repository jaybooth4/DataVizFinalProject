from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

BATCHSIZE = 1
lossXY = torch.nn.MSELoss()
lossL1 = torch.nn.L1Loss()

def main():
    playData = PBPDataset('../data/patternCategory.csv')
    rnn = PBPModel(4, 10, numLayers=1)
    optimizer = torch.optim.Adam(rnn.parameters(), lr=.01)

    for epoch in range(3000):
        for batch, labels in playData:
            hidden, loss = rnn.init_hidden(BATCHSIZE), 0
            for inputPoint, label in zip(batch, labels):
                output, hidden = rnn(inputPoint, hidden)
                loss += lossXY(output[0][0][0:2], label[0][0][0:2])
                loss += lossL1(output[0][0][2], label[0][0][2])
                loss += lossL1(output[0][0][3], label[0][0][3])
            print(loss)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    torch.save(rnn, "model/test.pt")

if __name__ == "__main__":
    main()
