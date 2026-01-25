dict = {}
ans = 0
for _ in range(10):
    N=int(input())
    if N in dict:
        dict[N] += 1
    else:
        dict[N] = 1
    ans += N

print(ans//10)
cnt = 0
for d in dict:
    if dict[d] > cnt:
        ans = d
        cnt = dict[d]
print(ans)