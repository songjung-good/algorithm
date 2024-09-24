N = int(input())
for i in range(31):
    now = 2 ** i
    if N == now:
        print(1)
        break
    elif N < now:
        print(0)
        break
    else:
        pass
