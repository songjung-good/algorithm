import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A_lst = list(map(int, input().split()))

A_lst.sort()

# 구간 합 계산
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A_lst[i - 1]

# 쿼리 처리
for _ in range(Q):
    L, R = map(int, input().split())
    print(prefix_sum[R] - prefix_sum[L - 1])
