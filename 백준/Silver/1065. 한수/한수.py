N = int(input())
ans = 99
if N < 100:
    print(N)
else:
    for n in range(100, N+1):
        num = str(n)
        a,b,c = int(num[0]), int(num[1]), int(num[2])
        gap = a - b
        if b - c == gap:
            ans += 1
    print(ans)
            