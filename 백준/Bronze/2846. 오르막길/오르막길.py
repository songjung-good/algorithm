N = int(input())
num_lst = list(map(int, input().split()))

low_num = 0
max_num = 0
max_gap = 0
for i in range(N):
    if i == 0:
        low_num = num_lst[i]
        max_num = num_lst[i]
    else:
        if max_num < num_lst[i]:
            max_num = num_lst[i]
            gap = max_num - low_num
            if max_gap < gap:
                max_gap = gap
        else:
            low_num = num_lst[i]
            max_num = num_lst[i]

print(max_gap)