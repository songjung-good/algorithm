# 코드를 작성해주세요
import heapq, sys
input = sys.stdin.readline

hq = []
N = int(input())
for _ in range(N):
    now = int(input())
    if now == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, now)

