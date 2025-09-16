import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    # 국가의 수 N, 비행기 종류 M
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())

    print(N-1)