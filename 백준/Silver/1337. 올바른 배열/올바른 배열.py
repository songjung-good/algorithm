N = int(input())
num_lst = []
for n in range(N):
    num_lst.append(int(input()))

num_lst.sort()

gap_lst = []
now = 0
for i in num_lst:
    num = i - now
    gap_lst.append(num)
    now = i

min_num = 4
for j in range(1, N):
    cnt = 4
    check = 0
    for k in range(j, N):
        check += gap_lst[k]
        if check < 5:
            cnt -= 1
    if cnt < min_num:
        min_num = cnt

# if min_num < 0:
#     min_num = 0
print(min_num)
