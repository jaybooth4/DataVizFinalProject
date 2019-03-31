import torch
import pandas as pd
from torch.utils.data import Dataset

class RNNDataset(Dataset):

    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)

    def __len__(self):
        # Number of rows
        return self.data.shape[0]

    def __getitem__(self, index):
        # Convert each tensor to a sample
        sample = torch.tensor(self.data.iloc[index])
        return sample


if __name__ == "__main__":
    ds = RNNDataset("data/play.csv")
    print(ds.__getitem__(5))
    print(ds.__len__())
    