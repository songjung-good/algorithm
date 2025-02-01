import sys
input = sys.stdin.readline

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


N = int(input())
lst = list(map(int, input().split()))
ans = 0

check = []
for n in range(1, N):
    if lst[n-1] > lst[n]:
        check.append(n-1)

if len(check) == 0:
    ans = N
elif len(check) > 1:
    ans = 0
else:
    if is_sorted(lst[:check[0]] + lst[check[0]+1:]):
        ans += 1
    if is_sorted(lst[:check[0]+1] + lst[check[0]+2:]):
        ans += 1

print(ans)