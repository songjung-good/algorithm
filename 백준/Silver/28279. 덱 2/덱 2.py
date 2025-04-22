import sys
from collections import deque
input = sys.stdin.readline

DECK = deque()
cnt = 0
N = int(input())
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        DECK.appendleft(order[1])
        cnt += 1
    elif order[0] == 2:
        DECK.append(order[1])
        cnt += 1
    elif order[0] == 3:
        if cnt == 0:
            print(-1)
        else:
            print(DECK.popleft())
            cnt -= 1
    elif order[0] == 4:
        if cnt == 0:
            print(-1)
        else:
            print(DECK.pop())
            cnt -= 1
    elif order[0] == 5:
        print(cnt)
    elif order[0] == 6:
        if cnt:
            print(0)
        else:
            print(1)
    elif order[0] == 7:
        if cnt:
            print(DECK[0])
        else:
            print(-1)
    elif order[0] == 8:
        if cnt:
            print(DECK[-1])
        else:
            print(-1)
