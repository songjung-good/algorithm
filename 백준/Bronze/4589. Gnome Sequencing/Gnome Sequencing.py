N = int(input())
print('Gnomes:')
for _ in range(N):
    lst = list(map(int, input().split()))
    lst1 = sorted(lst)
    lst2 = sorted(lst, reverse=True)
    if lst == lst1 or lst == lst2:
        print('Ordered')
    else:
        print('Unordered')