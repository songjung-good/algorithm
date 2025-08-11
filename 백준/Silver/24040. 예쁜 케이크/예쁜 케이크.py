T = int(input())
for _ in range(T):
    N = int(input())
    if N % 3 == 2:
        print("TAK")
    elif N % 9 == 0:
        print("TAK")
    else:
        print("NIE")