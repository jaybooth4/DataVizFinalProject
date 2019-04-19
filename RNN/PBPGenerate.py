from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch
import pandas as pd

torch.manual_seed(1)
OUTFILE = "output/generateTest.csv"
MODEL = "model/full.pt"

def main():
    rnn = torch.load(MODEL)

    hidden = rnn.init_hidden()
    output = rnn.init_input()
    outputs = []

    for _ in range(10):
        print("out")
        print(output)
        output, hidden = rnn(output, hidden)
        outputs.append(output.tolist()[0][0])

    df = pd.DataFrame(outputs)
    df.to_csv(OUTFILE, index=False, header=False)

if __name__ == "__main__":
    main()
