import sys, math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())
    if num in [0, 1, 2]:
        print(2)
    elif num == 3:
        print(3)
    else:
        while True:
            if num % 2 == 0:
                pass
            else:
                n = int(math.sqrt(num)) + 1
                check = 0
                for i in range(3, n, 2):
                    if num % i == 0:
                        check = 1
                        break
                if check == 0:
                    print(num)
                    break
            num += 1