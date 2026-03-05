import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    print(1)
    exit()

for i in range(N):
    num = -1
    cnt = -1
    for j in range(N-i):
        if num <= A[j]:
            num, cnt = A[j], j

    A[N-1-i], A[cnt] = A[cnt], A[N-1-i]
    if A == B:
        print(1)
        exit()

print(0)