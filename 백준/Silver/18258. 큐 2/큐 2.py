import sys
input = sys.stdin.readline

N = int(input())
q = [0] * N
fr, rear = -1, -1
for i in range(N):
    i = input().strip()
    if i == 'pop':
        if fr == rear:
            print(-1)
        else:
            fr += 1
            print(q[fr])
            q[fr] = 0
    elif i == 'size':
        print(rear - fr)
    elif i == 'empty':
        if fr == rear:
            print(1)
        else:
            print(0)
    elif i == 'front':
        if fr == rear:
            print(-1)
        else:
            print(q[fr+1])
    elif i == 'back':
        if fr == rear:
            print(-1)
        else:
            print(q[rear])
    else:
        a, b = i.split()
        rear += 1
        q[rear] = int(b)