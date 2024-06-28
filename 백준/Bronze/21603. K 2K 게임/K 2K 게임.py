A, B = map(int, input().split())
ans = []
B = B % 10
BB = (B*2) % 10
X = 0
for i in range(1, A+1):
    j = i
    if i >= 10:
        j = j % 10
    if j != B and j != BB:
        ans.append(i)
        X += 1
    else:
        pass

if X == 0:
    print(0)
else:
    print(X)
    print(*ans)