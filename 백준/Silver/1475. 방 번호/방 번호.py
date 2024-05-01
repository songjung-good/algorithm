import math
N = str(input())
cnt = [0] * 9

for i in N:
    now = int(i)
    if now == 9:
        cnt[6] += 1
    else:
        cnt[now] += 1

cnt[6] = math.ceil(cnt[6] / 2)
print(max(cnt))