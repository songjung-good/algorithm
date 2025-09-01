A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())

X = (A1*3 + B1*20 + C1*120)
Y = (A2*3 + B2*20 + C2*120)
if X == Y:
    print('Draw')
elif X > Y:
    print('Max')
else:
    print('Mel')