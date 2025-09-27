import torch

x = torch.rand(5, 3)
print(x[:, 1])

x = torch.rand(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size())
print(y.size())
print(z.size())

x = torch.rand(1)
print(x)
print(x.item())

print(torch.backends.mps.is_available())  # True se la GPU è utilizzabile
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

x = torch.ones(5, device=device)
y = torch.rand(5, device=device)
z = x + y
print(z)