num_lst = list(map(int, input().split(' ')))
ans = 'S'
for i in num_lst:
    if i == 0 or i == 1:
        pass
    else:
        ans = 'F'
print(ans)