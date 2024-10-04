T = int(input())
for t in range(T):
    lst = list(map(int, input().split()))
    lst.sort()
    new_lst = lst[1:4]
    if new_lst[2] - new_lst[0] >= 4:
        print('KIN')
    else:
        print(sum(new_lst))