# 코드를 작성해주세요
T = int(input())
lst = list(map(int, input().split()))
ans = 0
if T <= 2:
    ans += 508 * lst[0]
else:
    if lst[0] > lst[2]:
        ans += 508 * (lst[0] - lst[2])
    else:
        ans += 108 * (lst[2] - lst[0])

if T == 1:
    pass
elif 2 <= T <= 3:
    ans += 212 * lst[1]
else:
    if lst[1] > lst[3]:
        ans += 212 * (lst[1] - lst[3])
    else:
        ans += 305 * (lst[3] - lst[1])

if T == 5:
    ans += lst[4] * 707

print(ans * 4763)