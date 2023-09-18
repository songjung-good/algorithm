def quickSort(list):
    if len(list) <= 1:
        return list
 
    left = []
    right = []
    equal = []
    pivot = list[0]
    for i in list:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
 
    return quickSort(left) + equal + quickSort(right)
 
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    new_lst = quickSort(lst)
    ans = new_lst[N//2]
 
    print(f'#{t} {ans}')