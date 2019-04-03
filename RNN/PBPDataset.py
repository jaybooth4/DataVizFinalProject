import torch
import pandas as pd
from torch.nn.utils.rnn import pad_packed_sequence
import numpy as np

class PBPDataset:

    def __init__(self, CSVFile):
        self.data = pd.read_csv(CSVFile)[["game_id", "event_coord_x", "event_coord_y"]]
        gameDataframes = [self.data.loc[self.data["game_id"] == game_id, ["event_coord_x", "event_coord_y"]] for game_id in self.data["game_id"].unique()]
        self.batched = list(map(lambda game: torch.tensor(game.values, dtype=torch.float).view(1, -1, 2), gameDataframes))
        self.labels = list(map(lambda game: torch.tensor(np.append(game.values[1:], np.array([-1, -1])).reshape(-1, 2), dtype=torch.float).view(1, -1, 2), gameDataframes))
        self.numBatches = len(self.batched)
        self.index = 0

    def __len__(self):
        return self.numBatches

    def __next__(self):
        if self.index >= self.numBatches:
            raise StopIteration
        else:
            batch = self.batched[self.index]
            labels = self.labels[self.index]
            self.index += 1
            return batch, labels

    def __iter__(self):
        return self


if __name__ == "__main__":
    ds = PBPDataset("../data/pbp_final_small.csv")
    print(ds.__len__())
    print(ds.__next__())