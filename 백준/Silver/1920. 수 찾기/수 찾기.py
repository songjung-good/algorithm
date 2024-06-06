def bi_search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return bi_search(arr, target, start, mid-1)
    else:
        return bi_search(arr, target, mid+1, end)

N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
N_lst.sort()

# print(N, N_lst, M, M_lst)
for i in M_lst:
    ans = bi_search(N_lst, i, 0, N-1)
    print(ans)
