import sys
from collections import deque
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    if mid < len(arr) / 2:
        mid+=1
    l = arr[:mid]
    r = arr[mid:]

    left = merge_sort(l)
    right = merge_sort(r)
    return merge(left, right)

def merge(left, right):
    global cnt, answer
    left, right = deque(left), deque(right)
    result = deque([])

    while left and right:
        if left[0] < right[0]:
            ans = left.popleft()
            result.append(ans)
        else:
            ans = right.popleft()
            result.append(ans)
        cnt += 1
        if cnt == K:
            print(ans)
            exit()
    while left:
        ans = left.popleft()
        result.append(ans)
        cnt += 1
        if cnt == K:
            print(ans)
            exit()
    while right:
        ans = right.popleft()
        result.append(ans)
        cnt += 1
        if cnt == K:
            print(ans)
            exit()

    return result


A, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
answer = 0
sorted_lst = merge_sort(lst)
if cnt < K:
    answer = -1

print(answer)
