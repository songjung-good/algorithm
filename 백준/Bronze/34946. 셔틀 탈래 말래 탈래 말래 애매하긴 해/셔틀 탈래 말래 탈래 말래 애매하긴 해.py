A, B, C, D = map(int, input().split())

X = A+B

if D < X and D < C:
    print('T.T')
elif D < X and D >= C:
    print('Walk')
elif D >= X and D < C:
    print('Shuttle')
else:
    print('~.~')