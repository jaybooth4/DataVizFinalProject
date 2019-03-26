import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from .readData import RNNDataset

torch.manual_seed(1)

def main():
    # Define custom dataset
    playData = RNNDataset('data/play.csv')
    # Define data loader
    mn_dataset_loader = torch.utils.data.DataLoader(dataset=playData,
                                                    batch_size=2,
                                                    shuffle=False)
    
    for images, labels in mn_dataset_loader:
        # Feed the data to the model

if __name__ == "__main__":
    main()