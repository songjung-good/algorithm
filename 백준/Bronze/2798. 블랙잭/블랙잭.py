from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))

num_lst = list(combinations(lst, 3))
A = len(num_lst)

ans = 0
cnt = M
for i in range(A):
    now = sum(num_lst[i])
    if now <= M:
        B = M - now
        if B < cnt:
            ans = now
            cnt = B

print(ans)