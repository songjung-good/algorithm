N = int(input())

if N == 1:
    print('*')
else:
    for n in range(N):
        Number = n+1
        blank = N - Number
        star = n
        A = ' ' * blank
        B = '*' * star
        print(f'{A}{B}*{B}')
