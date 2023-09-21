def select(arr, num, n, stack=[]):
    if len(stack) == num:
        print(" ".join(map(str, stack)))
        return

    for i in arr[n:]:
        if i not in stack:
            select(arr, num, i, stack + [i])

N, M = map(int, input().split())
lst = list(range(1, N+1))
select(lst, M, 0)