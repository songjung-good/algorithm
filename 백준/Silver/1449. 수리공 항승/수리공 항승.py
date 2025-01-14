import sys
input = sys.stdin.readline

# L사이즈 테이프로 L개의 구멍을 한번에 막을 수 있다.
N, L = map(int, input().split())
hole = sorted(map(int, input().split()))

ans = 0
start = 0
while start < N:
    ans += 1
    end = hole[start] + L - 1
    while start < N and hole[start] <= end:
        start += 1

print(ans)
