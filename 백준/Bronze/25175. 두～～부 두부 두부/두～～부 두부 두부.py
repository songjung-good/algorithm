N, M, K = map(int, input().split())

FIND = (K - 3) % N
'''
10 7 0
'''
if FIND == 0:
    print(M)
else:
    X = FIND + M
    if X > N:
        X = X % N
    print(X)