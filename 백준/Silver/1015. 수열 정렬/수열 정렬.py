N = int(input())
lst = list(map(int, input().split()))
idx_lst = sorted([(lst[i], i) for i in range(N)])

ans = [0] * N
for idx, (_, i) in enumerate(idx_lst):
    ans[i] = idx

print(*ans)