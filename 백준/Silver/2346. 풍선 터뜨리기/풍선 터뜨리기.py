import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
N = int(input())
DECK = deque(list(map(int, input().split())))
num_lst = deque([i for i in range(1, N+1)])

ans = []
while DECK:
    now = DECK.popleft()
    ans.append(num_lst.popleft())
    if not DECK:
        break
    if now < 0:
        DECK.rotate(-now)
        num_lst.rotate(-now)
    else:
        DECK.rotate(-(now-1))
        num_lst.rotate(-(now-1))
print(*ans)
