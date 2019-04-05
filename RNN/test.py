from PBPDataset import PBPDataset
from PBPModel import PBPModel
import torch

torch.manual_seed(1)

lossCrossEntropy = torch.nn.NLLLoss()

# test1 = torch.randn(1, 5, dtype=torch.float)#torch.tensor([0, 1, 0], dtype=torch.float).view(3, 1)
# test2 = torch.empty(1, dtype=torch.long).random_(5)#torch.tensor([.1, .8, .1], dtype=torch.float).view(3, 1)
test1 = torch.tensor([.25, .7, .25], dtype=torch.float).view(1, -1)
test2 = torch.max(test1, 1)[1]
print(test1)
print(test2)
# print(torch.max(test1, 1)[1])
# print(lossCrossEntropy(test1, test2))
print(lossCrossEntropy(test1, torch.max(test1, 1)[1]))
# print(lossCrossEntropy(test1, test1))