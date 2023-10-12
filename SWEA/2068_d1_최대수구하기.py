
N = int(input())
X = int(1)

if X <= 1:
    for i in range(N):
        A = list(map(int, input().split()))
        A.sort()
        print("%s%s %d" %("#", X, A[9]))
        X += 1
elif N >= X:
        pass