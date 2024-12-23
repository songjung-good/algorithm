import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))

used = [0] * N
def perm(arr, n):
    if n == M:
        print(*arr)
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            arr.append(n_lst[i])
            perm(arr, n+1)
            arr.pop()
            used[i] = 0

perm([], 0)
