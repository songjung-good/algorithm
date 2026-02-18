# 코드를 작성해주세요
T = int(input())
for _ in range(T):
    N=int(input())
    if N == 1:
        print(0)
    else:
        for n in range(N):
            now = n + n**2
            if N > now:
                pass
            elif N == now:
                print(n)
                break
            else:
                print(n-1)
                break