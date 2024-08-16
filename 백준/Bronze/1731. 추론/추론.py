import sys
input = sys.stdin.readline

N = int(input())
num_lst = []
for n in range(N):
    num_lst.append(int(input()))

P = 0
Q = 0

for i in range(1, 3):
    num = num_lst[i] - num_lst[i - 1]
    if P == 0:
        P = num
    elif P != num:
        Q = num_lst[i] // num_lst[i-1]
        break

if Q == 0:
    print(num_lst[-1] + P)
else:
    print(num_lst[-1] * Q)
