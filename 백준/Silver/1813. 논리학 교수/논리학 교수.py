N = int(input())
N_lst = list(map(int, input().split()))
cnt = [0] * 51
for i in N_lst:
    cnt[i] += 1

for i in range(N, 0, -1):
    if cnt[i] == i:
        print(i)
        exit()

if cnt[0]:
    print(-1)
else:
    print(0)