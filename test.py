import os
os.environ['CUDA_DEVICE_ORDER']='PCI_BUS_ID'
import torch
print(torch.cuda.current_device())
a = torch.zeros(100,100000).to("cuda")
input()
