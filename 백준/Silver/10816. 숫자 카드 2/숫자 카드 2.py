# 코드를 작성해주세요
N = int(input())
lst = list(map(int, input().split()))
N_dict = {}
for l in lst:
    if l in N_dict:
        N_dict[l] += 1
    else:
        N_dict[l] = 1
M = int(input())
M_lst = list(map(int, input().split()))
ans = [0] * M
for m in range(M):
    if M_lst[m] in N_dict:
        ans[m] = N_dict[M_lst[m]]

print(*ans)