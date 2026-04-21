A, B = map(int, input().split())
if A == 0:
    if B == 0:
        print('=')
    elif B == 5:
        print('<')
    else:
        print('>')
elif A == 2:
    if B == 0:
        print('<')
    elif B == 2:
        print('=')
    else:
        print('>')
elif A == 5:
    if B == 2:
        print('<')
    elif B == 5:
        print('=')
    else:
        print('>')
else:
    if B in [1,3,4]:
        print('=')
    else:
        print('<')