N = int(input())
for n in range(1, N+1):
    print(n, end=' ')
    if n % 6 == 0:
        print('Go!', end=' ')
if n % 6:
    print('Go!')