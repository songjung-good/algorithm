# import sys
# input = sys.stdin.readline
X = input()
X_num = len(X)
Y = input()
Y_num = len(Y)
MAP = [[0] * (Y_num + 1) for _ in range(X_num + 1)]

for x in range(1, X_num+1):
    for y in range(1, Y_num+1):
        if X[x-1] == Y[y-1]:
            MAP[x][y] = MAP[x-1][y-1] + 1
        else:
            MAP[x][y] = max(MAP[x-1][y], MAP[x][y-1])

print(MAP[X_num][Y_num])