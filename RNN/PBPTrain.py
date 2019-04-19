from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

lossMSE = torch.nn.MSELoss()
lossCrossEntropy = torch.nn.CrossEntropyLoss()

def extractOutputFields(output):
    time = output[0][0][0]
    xy = output[0][0][1:3]
    ptsScored = output[0][0][3]
    leftRight = output[0][0][4:6].view(1, -1)
    eventType = output[0][0][6:].view(1, -1)
    return time, xy, ptsScored, leftRight, eventType

def extractLabelFields(label):
    timeLabel = label[0][0][0]
    xyLabel = label[0][0][1:3]
    ptsScoredLabel = label[0][0][3]
    
    # Convert to expected input of Cross entropy loss
    leftRightLabel = torch.max(label[0][0][4:6].view(1, -1), 1)[1]
    eventTypeLabel = torch.max(label[0][0][6:].view(1, -1), 1)[1]
    
    return timeLabel, xyLabel, ptsScoredLabel, leftRightLabel, eventTypeLabel



def main():
    playData = PBPDataset('../data/pbp_preprocessed_no_0_100k.csv')
    print("Read data...")
    featureSize = playData.getFeatureLength()
    rnn = PBPModel(featureSize, featureSize * 2, numLayers=1)
    optimizer = torch.optim.Adam(rnn.parameters(), lr=.015)

    for epoch in range(4):
        gameNum = 0
        for batch, labels in playData:
            hidden, loss = rnn.init_hidden(), 0
            for inputPoint, label in zip(batch, labels):
                output, hidden = rnn(inputPoint, hidden)

                time, xy, ptsScored, leftRight, eventType = extractOutputFields(output)
                timeLabel, xyLabel, ptsScoredLabel, leftRightLabel, eventTypeLabel = extractLabelFields(label)

                loss += lossMSE(time, timeLabel)
                loss += lossMSE(xy, xyLabel)
                loss += lossMSE(ptsScored, ptsScoredLabel)
                loss += lossCrossEntropy(leftRight, leftRightLabel)
                loss += lossCrossEntropy(eventType, eventTypeLabel)

            print("Game number: " + str(gameNum))
            print("Loss: " + str(loss))
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            gameNum += 1
    
    torch.save(rnn, "model/full_no_0_2.pt")

if __name__ == "__main__":
    main()