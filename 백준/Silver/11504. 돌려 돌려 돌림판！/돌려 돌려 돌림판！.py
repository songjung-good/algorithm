import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
# 테스트케이스 T
for t in range(T):
    # 돌림판 N등분, 자릿수 M
    N, M = map(int, input().split())
    # 숫자 X, Y
    X = int(input().replace(" ",""))
    Y = int(input().replace(" ",""))
    # 돌림판 숫자
    Q = deque(map(int, input().split()))

    cnt = 0
    for n in range(N):
        num = ''
        for m in range(M):
            num += str(Q[m])
        num = int(num)
        if num >= X and num <= Y:
            cnt += 1
        Q.append(Q.popleft())

    print(cnt)