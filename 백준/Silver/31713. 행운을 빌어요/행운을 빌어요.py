import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ans = 0
    A, B = map(int, input().split())
    if 3*A <= B <= 4*A:
        print(0)
    # 잎이 부족
    elif 3*A > B:
        cnt = 3*A - B
        print(cnt)
    # 줄기가 부족
    else:
        cnt = B - (4 * A)
        if cnt % 4 == 0:
            print(cnt//4)
        elif cnt % 4 == 3:
            print(cnt // 4 + 1)
        elif cnt % 4 == 2:
            if A + (cnt//4) >= 1:
                print(cnt // 4 + 1)
            else:
                print(cnt // 4 + 2)
        else:
            if A + (cnt//4) >= 2:
                print(cnt // 4 + 1)
            elif A + (cnt//4) == 1:
                print(cnt // 4 + 2)
            else:
                print(cnt // 4 + 3)