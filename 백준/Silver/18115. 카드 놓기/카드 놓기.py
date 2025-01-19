from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
card = deque(range(1, N+1))
deck = [0] * N

for n in range(N):
    if lst[n] == 1:
        now = card.popleft()
    elif lst[n] == 2:
        temp = card.popleft()
        now = card.popleft()
        card.appendleft(temp)
    elif lst[n] == 3:
        now = card.pop()
    deck[now-1] = N - n

print(*deck)