import sys
input = sys.stdin.readline

lst = [1, 1]

K = int(input())
cnt = 1
x, y = 0, 1
while K >= cnt:
    if K == cnt:
        x, y = lst[1] - lst[0], lst[0]
        break
    else:
        lst[0], lst[1] = lst[1], lst[0] + lst[1]
        cnt += 1

print(x, y)