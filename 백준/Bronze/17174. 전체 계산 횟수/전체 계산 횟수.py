import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = N
while True:
    A = N//M
    ans = ans + A
    N = A
    if N < M:
        break
print(ans)