from time import time

start = time()
m = 10**6
n = "1" * m
while n:
    x = n[0]
    n = n[1:]
print(time()-start)

start = time()
n = "1" * m
for i in range(m):
    n[i]
print(time()-start)
