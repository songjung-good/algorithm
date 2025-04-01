# 코드를 작성해주세요
T = int(input())
for _ in range(T):
    d, n, s, p = map(int, input().split())
    P = n * p + d
    S = s * n
    if S > P:
        print('parallelize')
    elif S < P:
        print('do not parallelize')
    else:
        print('does not matter')