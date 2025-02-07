import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))

start1 = 0
cnt1 = 0
start2 = 0
cnt2 = 0
for n in range(N):
    if N_lst[n] % 2 == 0:
        cnt1 += n - start1
        start1 += 1
    else:
        cnt2 += n - start2
        start2 += 1

print(min(cnt1, cnt2))
