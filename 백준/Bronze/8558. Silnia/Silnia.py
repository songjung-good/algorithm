n = int(input())
ans = 1
if n <= 1:
    print(1)
else:
    for i in range(2, n+1):
        ans = (ans * i) % 10
    print(ans)