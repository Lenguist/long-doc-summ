import torch

if torch.cuda.is_available():
    print("PyTorch can use GPUs!")
else:
    print("PyTorch cannot use GPUs.")
