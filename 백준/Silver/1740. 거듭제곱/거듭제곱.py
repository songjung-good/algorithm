N = int(input())
num = format(N, 'b')
cnt = len(num) - 1

ans = 0
for n in num:
    if n == '1':
        ans += 3 ** cnt
    cnt -=1

print(ans)
