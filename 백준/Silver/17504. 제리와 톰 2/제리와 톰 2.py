import sys
input = sys.stdin.readline

N = int(input())
NUM = list(map(int, input().split()))
A = 1
B = NUM[-1]

for i in range(2, N+1):
    A = A + B * NUM[-i]
    B = B
    A, B = B, A

A = B - A
print(A, B)