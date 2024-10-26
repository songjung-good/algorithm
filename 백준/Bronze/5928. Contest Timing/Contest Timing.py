D, H, M = map(int, input().split())

NOW = [D - 11, H - 11, M - 11]

if NOW[2] < 0:
    NOW[1] -= 1
    NOW[2] += 60
if NOW[1] < 0:
    NOW[0] -= 1
    NOW[1] += 24

ans = 0

ans = (NOW[0] * 24 + NOW[1]) * 60 + NOW[2]

if ans < 0:
    print(-1)
else:
    print(ans)