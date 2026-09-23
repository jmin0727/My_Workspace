import torch

print("PyTorch :", torch.__version__)
print("CUDA :", torch.version.cuda)
print("GPU 사용 :", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU :", torch.cuda.get_device_name(0))


