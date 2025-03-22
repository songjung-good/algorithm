N = int(input())
N_lst = list(map(int, input().split()))
M_lst = [0] * N
ans = 0
for n in range(1, N):
    M_lst[n] += N_lst[N - n] + M_lst[n-1]

for n in range(1, N):
    ans += M_lst[N-n] * N_lst[n-1]

print(ans%1000000007)