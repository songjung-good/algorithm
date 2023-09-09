N = int(input())


a = N // 5
ans = 99999999

for i in range(a+1):
    c = 5 * i
    d = (N - c) // 3
    if c + d * 3 == N:
        if ans > i+d:
            ans = i+d

if ans == 99999999:
    ans = -1

print(ans)
