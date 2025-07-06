import sys
input = sys.stdin.readline

a, b, c = sorted(map(int,input().split()))
ans = 0
A = 0
B = 0
if a == b and b == c:
    ans = 2
if a ** 2 + b ** 2 == c ** 2:
    ans = 1

print(ans)
