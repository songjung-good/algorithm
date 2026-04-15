N, M = input().split()
size = len(N) * int(N)
if size <= int(M):
    print(N * int(N))
else:
    ans = N * (int(M) // len(N) + 1)
    print(ans[:int(M)])

