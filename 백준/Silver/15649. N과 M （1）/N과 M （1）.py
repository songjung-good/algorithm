def select(arr, num, stack=[]):
    if len(stack) == num:
        print(" ".join(map(str, stack)))
        return

    for i in arr:
        if i not in stack:
            select(arr, num, stack + [i])

N, M = map(int, input().split())
lst = list(range(1, N+1))
select(lst, M)