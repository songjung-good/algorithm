N = int(input())
lst = list(map(int, input().split()))
cnt = 1
now = lst[0]
seg = []
for i in range(1, N):
    if now == lst[i]:
        cnt += 1
    else:
        now = lst[i]
        seg.append(cnt)
        cnt = 1
seg.append(cnt)

ans = seg[0]
for i in range(1, len(seg)):
    ans = max(ans, (seg[i] + seg[i-1]))

print(ans)
