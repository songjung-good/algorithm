import sys
input = sys.stdin.readline

N = int(input())
num = []
for n in range(N):
    A = int(input())
    num.append(A)

num.sort()
for a in num:
    print(a)