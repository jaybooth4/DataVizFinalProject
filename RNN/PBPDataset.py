import torch
import pandas as pd
from torch.nn.utils.rnn import pad_packed_sequence

class PBPDataset:

    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.batched = self.data.groupby('game_id').apply(list)
        print(self.batched)
        self.numBatches = self.batched.shape[0]
        self.index = 0

    def __len__(self):
        return self.numBatches

    def __next__(self):
        if self.index >= self.numBatches:
            raise StopIteration
        else:
            batch = self.data.iloc[self.index]
            self.index += 1
            return batch

    def __iter__(self):
        return self


if __name__ == "__main__":
    ds = PBPDataset("data/pbp_final_small.csv")
    print(ds.__len__())
    print(type(ds.__next__()))
    print(ds.__next__())
    print(ds.__next__().values)
    print(ds.__next__().values.shape)
    