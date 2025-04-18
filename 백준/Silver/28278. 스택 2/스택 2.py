import sys
input = sys.stdin.readline

N = int(input())
STACK = []
now = 0
for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        STACK.append(order[1])
        now += 1
    elif order[0] == 2:
        if now == 0:
            print(-1)
        else:
            print(STACK.pop())
            now -= 1
    elif order[0] == 3:
        print(now)
    elif order[0] == 4:
        if now == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 5:
        if now == 0:
            print(-1)
        else:
            print(STACK[-1])