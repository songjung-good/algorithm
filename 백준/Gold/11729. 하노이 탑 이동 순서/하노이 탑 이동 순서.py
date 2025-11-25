import sys
from datetime import timedelta
input = sys.stdin.readline

def hanoi(cnt, start, end, mid):
    if cnt == 1:
        print(start, end)

    else:
        hanoi(cnt-1, start, mid, end)
        print(start, end)
        hanoi(cnt-1, mid, end, start)

N = int(input())
ans = 1
now = 1

while now < N:
    ans = ans * 2 + 1
    now += 1
print(ans)

hanoi(N, 1, 3, 2)