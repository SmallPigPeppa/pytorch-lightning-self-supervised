import torch

msize = [1000, 1000, 1000]
n=4
a=[]
for i in range(n):
    a.append(torch.rand(size=msize).cuda(i))
while True:
    for i in range(n):
        a[i]=a[i]*2+a[i]
