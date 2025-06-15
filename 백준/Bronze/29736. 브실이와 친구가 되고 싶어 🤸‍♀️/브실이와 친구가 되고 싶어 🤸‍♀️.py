# 코드를 작성해주세요
A, B = map(int, input().split())
K, X = map(int, input().split())

min_num = K - X
max_num = K + X

cnt = min(B, max_num) - max(A, min_num)
if min_num > B or max_num < A:
    print('IMPOSSIBLE')
else:
    print(cnt+1)