import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        if N_lst[mid] == target:
            return True
        elif N_lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()
M = int(input())
M_lst = list(map(int, input().split()))

ans_lst = [0] * M
for m in range(M):
    num = M_lst[m]
    if binary_search(num):
        ans_lst[m] = 1

print(*ans_lst)