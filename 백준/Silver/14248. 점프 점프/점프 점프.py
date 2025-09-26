import sys
input = sys.stdin.readline

def DFS(s):
    if V[s]:
        return
    else:
        V[s] = 1
        size = lst[s]
        R = s + size
        L = s - size

        if R < N:
            DFS(R)
        if L >= 0:
            DFS(L)

N = int(input())
lst = list(map(int, input().split()))
S = int(input()) - 1

V = [0] * N

DFS(S)

print(sum(V))