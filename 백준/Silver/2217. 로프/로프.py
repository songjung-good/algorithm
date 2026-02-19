N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

ans = 0
for n in range(N):
    max_w = ropes[n] * (n+1)
    if max_w > ans:
        ans = max_w

print(ans)