import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = deque(list(map(int, input().split())))
B = deque(list(map(int, input().split())))
M = int(input())
C = deque(list(map(int, input().split())))

check = deque([])
for i in range(N):
    if A[i] == 0:
        check.append(B[i])

for c in C:
    check.appendleft(c)
    print(check.pop(), end=' ')
