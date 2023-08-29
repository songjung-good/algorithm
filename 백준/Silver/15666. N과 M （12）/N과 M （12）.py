def dfs(n):

    if len(s) == M:
        s.sort()
        new_s = tuple(s)
        if check.get(new_s, 0) == 0:
            check[new_s] = 1
            print(*s)
        return

    for i in range(n, N):
        s.append(lst[i])
        dfs(i)
        s.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []
check = {}
dfs(0)