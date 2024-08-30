import sys

input = sys.stdin.readline

def push(num):
    global STACK, now
    STACK.append(num)
    now = now + 1


def pop():
    global STACK, now
    if now == -1:
        res = -1
    else:
        res = STACK.pop()
        now = now - 1
    return res


def size():
    global now
    return now + 1


def empty():
    global now
    if now == -1:
        res = 1
    else:
        res = 0
    return res


def top():
    global STACK, now
    if now == -1:
        res = -1
    else:
        res = STACK[now]
    return res


STACK = []
now = -1
X = int(input())
for x in range(X):
    lst = input().split()
    func = lst[0]
    if func == 'push':
        push(lst[1])
    elif func == 'pop':
        print(pop())
    elif func == 'size':
        print(size())
    elif func == 'empty':
        print(empty())
    elif func == 'top':
        print(top())
