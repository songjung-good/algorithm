N = int(input())

for n in range(1, N+1):
    num = 0
    if n == N:
        print(0)
        exit()
    else:
        num += n
        for i in str(n):
            num += int(i)
        if num == N:
            print(n)
            exit()