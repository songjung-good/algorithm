t = int(input())
for i in range(t):
    n = int(input())
    win = 0
    for j in range(n):
        A, B = map(str, input().split())
        if A == B:
            pass
        else:
            if A == 'R':
                if B == 'S':
                    win += 1
                else:
                    win -= 1
            if A == 'S':
                if B == 'P':
                    win += 1
                else:
                    win -= 1
            if A == 'P':
                if B == 'R':
                    win += 1
                else:
                    win -= 1
    if win == 0:
        print('TIE')
    elif win < 0:
        print('Player 2')
    else:
        print('Player 1')