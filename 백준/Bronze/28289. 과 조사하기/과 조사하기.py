P = int(input())
X = 0
Y = 0
Z = 0
K = 0
for i in range(P):
    G, C, N = map(int, input().split())
    if G == 1:
        K += 1
    else:
        if C == 1 or C == 2:
            X += 1
        elif C == 3:
            Y += 1
        else:
            Z += 1
print(X)
print(Y)
print(Z)
print(K)