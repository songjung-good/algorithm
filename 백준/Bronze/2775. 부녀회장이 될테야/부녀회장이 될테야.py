T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    APT = [[i + 1 for i in range(n)] for _ in range(k + 1)]
    for i in range(k):
        APT[i+1][0] = 1
        for j in range(1, n):
            APT[i+1][j] = sum(APT[i][0:j+1])
    print(APT[k][n-1])
