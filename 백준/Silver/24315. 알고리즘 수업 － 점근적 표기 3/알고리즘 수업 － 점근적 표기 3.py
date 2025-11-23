a1, a0 = map(int,input().split())
c1, c2 = map(int,input().split())
n0 = int(input())
ans = 1
while True:
    if c1* n0 <= a1 * n0 + a0 and a1 * n0 + a0 <= c2 * n0:
        pass
    else:
        ans = 0
        break
    if n0 > 100:
        break
    n0 += 1

print(ans)