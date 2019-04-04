import torch
import pandas as pd
from torch.nn.utils.rnn import pad_packed_sequence
import numpy as np

# FEATURES = ["event_coord_x", "event_coord_y", "elapsed_time_sec", "category"]
# FEATURES = ["event_coord_x", "event_coord_y", "elapsed_time_sec"]
# FEATURES = ["elapsed_time_sec"]
FEATURES = ["event_coord_x", "event_coord_y", "category"]
# FEATURES = ["event_coord_x", "event_coord_y"]
# FEATURES = ["category"]

class PBPDataset:

    def __init__(self, CSVFile):
        data = pd.read_csv(CSVFile)[["game_id"] + FEATURES]
        # data["event_coord_x"] = data["event_coord_x"] / 1128.0
        # data["event_coord_y"] = data["event_coord_y"] / 600.0
        gameDataframes = [data.loc[data["game_id"] == game_id, FEATURES] for game_id in data["game_id"].unique()]
        self.batched = list(map(lambda game: torch.tensor(game.values[:-1], dtype=torch.float).view(-1, 1, 1, len(FEATURES)), gameDataframes))
        self.labels = list(map(lambda game: torch.tensor(game.values[1:], dtype=torch.float).view(-1, 1, 1, len(FEATURES)), gameDataframes))
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
        self.index = 0
        return self

if __name__ == "__main__":
    ds = PBPDataset("../data/pbp_final_small.csv")
    print(ds.__len__())
    print(ds.__next__())