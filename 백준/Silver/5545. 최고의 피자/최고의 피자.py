import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
D_lst = [int(input()) for _ in range(N)]
D_lst.sort(reverse=True)

max_cal = int(C / A)

D_cal = C
for i in range(N):
    D_cal += D_lst[i]
    now = int(D_cal / (A + B * (i+1)))
    if max_cal < now:
        max_cal = now

print(max_cal)
