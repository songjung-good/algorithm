def dfs(n):
    if len(s) == M:
        print(*s)
        return

    for i in range(n, N):
        x = lst[i]
        s.append(x)
        dfs(i)
        s.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []
dfs(0)