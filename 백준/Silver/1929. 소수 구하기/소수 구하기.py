import sys, math
input = sys.stdin.readline

def prime(a, b):
    past = 2
    for i in range(a, b+1):
        if i == 1:
            pass
        elif i == 2:
            print(2)
        else:
            check = True
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    check = False
                    break
            if check:
                print(i)
    exit()

M, N = map(int,input().split())
prime(M, N)
