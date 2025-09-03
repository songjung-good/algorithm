N = int(input())
size = 0
while True:
    if N // (9 ** size) > 0:
        size += 1
    else:
        break

ans = ''

for i in range(size):
    now = N % 9
    ans = str(now) + ans
    N = N // 9

print(ans)
