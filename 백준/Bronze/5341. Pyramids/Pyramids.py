A = 1
while A != 0:
    A = int(input())
    ans = 0
    if A == 0:
        break
    else:
        for i in range(A):
            ans += i+1
        print(ans)