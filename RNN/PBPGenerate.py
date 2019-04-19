from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch
import pandas as pd

torch.manual_seed(1)
OUTFILE = "output/generate.csv"
MODEL = "model/full_no_0.pt"

def main():
    rnn = torch.load(MODEL)

    hidden = rnn.init_hidden()
    output = rnn.init_input()
    outputs = []

    playData = PBPDataset('../data/pbp_preprocessed_small.csv')

    for batch, labels in playData:
        hidden= rnn.init_hidden()
        for inputPoint, label in zip(batch, labels):
            output, hidden = rnn(inputPoint, hidden)
            outputs.append(output.tolist()[0][0])

    df = pd.DataFrame(outputs)
    df.to_csv(OUTFILE, index=False, header=False)

if __name__ == "__main__":
    main()
