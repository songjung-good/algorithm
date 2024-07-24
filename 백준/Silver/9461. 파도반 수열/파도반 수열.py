import sys
input = sys.stdin.readline

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