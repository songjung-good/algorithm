from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
D = 1
choco = deque([])

cnt = 0
while D < K:
    choco.appendleft(D)
    cnt += 1
    D = 2 ** cnt

print(D, end=' ')

if D == K:
    print(0)
else:
    size = 0
    CNT = 0
    while K > size:
        now = choco.popleft()
        if size + now > K:
            pass
        else:
            size += now
        CNT += 1

    print(CNT)