'''
B = A * a + b
C = B * a + b

b = B - A * a

C = B * a + B - A * a
C = (B - A)a + B
C - B = (B - A) * a
'''

N = int(input())
lst = list(map(int, input().split()))

check = True
if N == 1:
    print('A')
elif N == 2:
    if lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')
else:
    A = lst[0]
    B = lst[1]
    C = lst[2]
    X = B - A
    Y = C - B
    if X == 0:
        for i in range(2,N):
            if lst[i] - lst[i-1] != lst[i-1] - lst[i-2]:
                print('B')
                exit()
        print(lst[-1] + lst[-1] - lst[-2])

    else:
        a = Y / X
        b = B - (A*a)
        if a != int(a):
            print('B')
        else:
            a = int(a)
            b = int(b)
            for i in range(1, N):
                if lst[i] == lst[i-1] * a + b:
                    pass
                else:
                    print('B')
                    exit()
            print(lst[-1] * a + b)


