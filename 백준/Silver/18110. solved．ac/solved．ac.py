import sys
input = sys.stdin.readline

N = int(input())
A = (N / 10 * 1.5) + 0.5
B = int(A)
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
C = sum(lst[int(A):N - int(A)])
if C == 0:
    print(0)
else:
    diff = C / (N-(2*B)) + 0.5
    print(int(diff))