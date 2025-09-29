import sys
input = sys.stdin.readline

N = int(input())
ans = 0
V = [False] * N
V1 = [False] * (2 * N)
V2 = [False] * (2 * N)

def DFS(row):
    global ans
    if row == N:
        ans += 1
        return
    for col in range(N):
        if V[col] or V1[row + col] or V2[row - col]:
            continue
        V[col] = V1[row + col] = V2[row - col] = True
        DFS(row + 1)
        V[col] = V1[row + col] = V2[row - col] = False

DFS(0)
print(ans)