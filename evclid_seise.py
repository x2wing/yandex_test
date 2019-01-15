N = 49
A = set(range(N))
B = {k for i in range(2, int(N ** 0.5)) for k in range(i * i, N, i)}

A = [1] * N
edge = int(N ** 0.5)
for i in range(2, edge):
    for k in range(i * i, N, i):
        A[k] = 0

for i in range(2,N):
    if A[i]:
        print(i)
