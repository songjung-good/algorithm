N = int(input())
for _ in range(N):
    a, b = input().split()
    if a == b:
        print('OK')
    else:
        print('ERROR')