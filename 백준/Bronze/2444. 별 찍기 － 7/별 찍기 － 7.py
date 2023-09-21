A = int(input())

for i in range(1, A+1):
    B = 2 * i - 1
    blank = " " * (A-i)
    star = "*" * (B)
    print(f'{blank}{star}')

for j in range(A-1, 0, -1):
    C = 2 * j - 1
    blank = " " * (A-j)
    star = "*" * (C)
    print(f'{blank}{star}')