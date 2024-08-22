T = int(input())
for t in range(T):
    N = int(input())
    lst1 = list(map(str, input().split()))
    lst2 = list(map(str, input().split()))
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        print('NOT CHEATER')
    else:
        print('CHEATER')