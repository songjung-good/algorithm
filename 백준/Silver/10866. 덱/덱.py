import sys
input = sys.stdin.readline

N = int(input())
deck = []
for _ in range(N):
    lst = list(map(str, input().split()))
    order = lst[0]
    if order == 'push_front':
        deck.insert(0, lst[1])
    elif order == 'push_back':
        deck.append(lst[1])
    elif order == 'pop_front':
        if deck:
            print(deck.pop(0))
        else:
            print(-1)
    elif order == 'pop_back':
        if deck:
            print(deck.pop(-1))
        else:
            print(-1)
    elif order == 'size':
        print(len(deck))
    elif order == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif order == 'back':
        if deck:
            print(deck[-1])
        else:
            print(-1)