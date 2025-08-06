# 코드를 작성해주세요
from fractions import Fraction
T = int(input())
for _ in range(T):
    # 고양이 수 N, 과자 수 M
    N, M = map(int, input().split())
    cat = [0] * N
    for _ in range(M):
        lst = list(map(int, input().split()))
        num = lst[0]
        for n in range(1, N+1):
            if lst[n] == 0:
                pass
            else:
                cat[n-1] += Fraction(lst[n], num)
    print(max(cat) - min(cat))
