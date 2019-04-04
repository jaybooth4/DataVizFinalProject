from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

BATCHSIZE = 1
lossXY = torch.nn.MSELoss()
lossTime = torch.nn.L1Loss()
adjustCat = torch.nn.Sigmoid()
lossCat = torch.nn.BCELoss()

def main():
    playData = PBPDataset('../data/pattern.csv')

    rnn = PBPModel(3, 3, numLayers=1)

    optimizer = torch.optim.Adam(rnn.parameters(), lr=.1)

    for epoch in range(3000):
        for batch, labels in playData:

            # for name, par in rnn.named_parameters():
            #     print(name, par)


            hidden, loss = rnn.init_hidden(BATCHSIZE), 0
            for inputPoint, label in zip(batch, labels):
                output, hidden = rnn(inputPoint, hidden)
                loss += lossXY(output[0][0][0:2], label[0][0][0:2])
                # loss += lossTime(output[0][0][2], label[0][0][2])
                cat = adjustCat(output[0][0][2])
                loss += lossCat(cat, label[0][0][2])

            print(loss)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    
    torch.save(rnn, "model/test.pt")

if __name__ == "__main__":
    main()
