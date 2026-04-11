T = int(input())
for _ in range(T):
    n, x = input().split() 
    if x == 'kg':
        a = float(n) * 2.2046
        print(f'{a:.4f} lb')
    elif x == 'lb':
        a = float(n) * 0.4536
        print(f'{a:.4f} kg')
    elif x == 'l':
        a = float(n) * 0.2642
        print(f'{a:.4f} g')
    elif x == 'g':
        a = float(n) * 3.7854
        print(f'{a:.4f} l')
        