# 코드를 작성해주세요
import sys, math
input = sys.stdin.readline

M = int(input())
N = int(input())

def check(i):
    x = int(math.sqrt(i)) + 1
    for j in range(2, x):
        if i % j == 0:
            return False
    return True

lst = []
for i in range(M, N+1):
    if i == 1:
        pass
    elif i < 4:
        lst.append(i)
    else:
        now=check(i)
        if now:
            lst.append(i)

A = sum(lst)
if A == 0:
    print(-1)
else:
    print(A)
    print(min(lst))