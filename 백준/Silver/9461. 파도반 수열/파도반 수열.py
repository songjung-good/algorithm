import sys
input = sys.stdin.readline

def CHECK(CNT, N, SIDE):
    if CNT >= N:
        return SIDE[N-1]
    else:
        TRI(CNT, N, SIDE)

def TRI(CNT, N, SIDE):
    for i in range(CNT, N):
        new_num = SIDE[i-2] + SIDE[i-1]
        SIDE.append(new_num)
    return CHECK(N, N, SIDE)

T = int(input())
SIDE = [1, 1, 1]
for t in range(T):
    CNT = len(SIDE)
    N = int(input())
    for i in range(CNT, N):
        new_num = SIDE[i-3] + SIDE[i-2]
        SIDE.append(new_num)
    ans = SIDE[N-1]
    print(ans)