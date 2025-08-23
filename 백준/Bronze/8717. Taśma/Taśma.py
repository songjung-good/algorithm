N = int(input())
lst = list(map(int, input().split()))

prefix1 = [0] * (N + 1)
prefix2 = [0] * (N + 1)
prefix1[1] = lst[0]
prefix2[N - 1] = lst[N - 1]

min_gap = float('inf')
for n in range(1, N):
    n2 = N - n - 1
    prefix1[n + 1] = lst[n] + prefix1[n]
    prefix2[n2] = lst[n2] + prefix2[n2 + 1]

for i in range(1, N):
    gap = abs(prefix1[i] - prefix2[i])
    if gap < min_gap:
        min_gap = gap

print(min_gap)
