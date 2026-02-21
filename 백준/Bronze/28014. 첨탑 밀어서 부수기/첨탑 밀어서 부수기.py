N = int(input())
lst = list(map(int, input().split()))
cnt = 1

for n in range(1, N):
    if lst[n-1] <= lst[n]:
        cnt += 1

print(cnt)