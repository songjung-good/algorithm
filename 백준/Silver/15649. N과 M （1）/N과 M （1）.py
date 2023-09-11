def dfs(c):
    if c == K:
        print(*subset)
        return

    for i in range(1, N + 1):
        if i not in subset:
            subset.append(i)
            dfs(c + 1)
            subset.pop()


N, K = map(int, input().split())
subset = []
dfs(0)