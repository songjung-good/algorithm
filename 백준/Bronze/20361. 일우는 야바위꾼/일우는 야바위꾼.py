N, X, K = map(int, input().split())
CUP = [0] * N
CUP[X-1] = 1
for _ in range(K):
    A, B = map(int, input().split())
    CUP[A-1], CUP[B-1] = CUP[B-1], CUP[A-1]

print(CUP.index(1) + 1)
