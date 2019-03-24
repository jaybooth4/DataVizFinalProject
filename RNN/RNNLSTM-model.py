import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

def main():
    # Define transforms
    transformations = transforms.Compose([])
    # Define custom dataset
    custom_mnist_from_csv = \
        CustomDatasetFromCSV('../data/mnist_in_csv.csv',
                             28, 28,
                             transformations)
    # Define data loader
    mn_dataset_loader = torch.utils.data.DataLoader(dataset=custom_mnist_from_csv,
                                                    batch_size=10,
                                                    shuffle=False)
    
    for images, labels in mn_dataset_loader:
        # Feed the data to the model

if __name__ == "__main__":
    main()