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
    playData = PBPDataset('../data/patternCategory.csv')

    rnn = PBPModel(4, 8, numLayers=1)

    optimizer = torch.optim.Adadelta(rnn.parameters(), lr=.1)

    for epoch in range(3000):
        for batch, labels in playData:

            hidden, loss = rnn.init_hidden(BATCHSIZE), 0
            for inputPoint, label in zip(batch, labels):
                output, hidden = rnn(inputPoint, hidden)
                loss += lossXY(output[0][0][0:2], label[0][0][0:2])
                loss += lossTime(output[0][0][2], label[0][0][2])
                cat = adjustCat(output[0][0][3])
                loss += 5 * lossCat(cat, label[0][0][3])
            print(loss)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # print(loss)
            # print(dir(optimizer))
            # print(optimizer.param_groups)
            # print(optimizer.state)
            # optimizer.zero_grad()
            # lossTimeVal.backward(retain_graph=True)
            # for param in rnn.parameters():
            #     print(param.grad.data.sum())
            # optimizer.step()

            # optimizer.zero_grad()
            # lossXYVal.backward(retain_graph=True)
            # for param in rnn.parameters():
            #     print(param.grad.data.sum())
            # optimizer.step()
            


    
    torch.save(rnn, "model/test.pt")

if __name__ == "__main__":
    main()
