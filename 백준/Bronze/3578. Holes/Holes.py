H = int(input())
if H == 0:
    print(1)
elif H == 1:
    print(0)
elif H % 2 == 1:
    print('4' + '8'*(H//2))
else:
    print('8' * (H//2))