N = int(input())
mirror = [input() for _ in range(N)]
K = int(input())
ans = [['a']*N for _ in range(N)]

if K == 1:
    ans = mirror
    for i in range(N):
        print(''.join(ans[i][0:N]))
elif K == 2:
    for i in range(N):
        for j in range(N):
            ans[i][j] = mirror[i][N-1-j]
        print(''.join(ans[i][0:N]))
else:
    for i in range(N):
        for j in range(N):
            ans[i][j] = mirror[N-1-i][j]
        print(''.join(ans[i][0:N]))
