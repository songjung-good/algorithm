import sys
input = sys.stdin.readline

n = int(input())
start, end = 0, n
ans = 0
check = 0

while start < end:
    mid = (start+end) // 2
    num = mid ** 2
    if num >= n:
        end = mid
    else:
        start = mid + 1

if start ** 2 >= n:
    print(start)
else:
    print(start+1)