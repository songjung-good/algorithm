# 코드를 작성해주세요
N, M = map(int, input().split())
ans = 0
for _ in range(N):
    o = 0
    x = 0
    for i in input():
        if i == 'O':
            o += 1
        else:
            x += 1
    if o > x:
        ans += 1
print(ans)