import torch
import pandas as pd
from torch.nn.utils.rnn import pad_packed_sequence
import numpy as np

FEATURES = ["elapsed_time_sec","event_coord_x","event_coord_y","points_scored","team_basket_left","team_basket_right",\
    "event_type_assist","event_type_attemptblocked","event_type_block","event_type_flagrantone","event_type_freethrowmade",\
    "event_type_freethrowmiss","event_type_jumpball","event_type_kickball","event_type_laneviolation","event_type_lineupchange",\
    "event_type_offensivefoul","event_type_openinbound","event_type_opentip","event_type_personalfoul","event_type_rebound",\
    "event_type_shootingfoul","event_type_teamtimeout","event_type_technicalfoul","event_type_threepointmade","event_type_threepointmiss",\
    "event_type_turnover","event_type_twopointmade","event_type_twopointmiss"]

class PBPDataset:

    def __init__(self, CSVFile):
        data = pd.read_csv(CSVFile)[["game_id"] + FEATURES]
        gameDataframes = [data.loc[data["game_id"] == game_id, FEATURES] for game_id in data["game_id"].unique()]
        self.batched = list(map(lambda game: torch.tensor(game.values[:-1], dtype=torch.float).view(-1, 1, 1, len(FEATURES)), gameDataframes))
        self.labels = list(map(lambda game: torch.tensor(game.values[1:], dtype=torch.float).view(-1, 1, 1, len(FEATURES)), gameDataframes))
        self.numBatches = len(self.batched)
        self.featureLength = len(FEATURES)
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

    def getFeatureLength(self):
        return self.featureLength

if __name__ == "__main__":
    ds = PBPDataset("../data/pbp_preprocessed_small.csv")
    print(ds.__len__())
    print(ds.__next__())