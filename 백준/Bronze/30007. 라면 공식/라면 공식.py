T = int(input())
for t in range(T):
    A, B, X = map(int, input().split())
    ans = A * (X-1) + B
    print(ans)