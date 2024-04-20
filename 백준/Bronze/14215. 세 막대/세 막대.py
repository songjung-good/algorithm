a, b, c = map(int, input().split())
num_lst = [a, b, c]
num_lst.sort()
long_bar = num_lst[2]
ex_bar = num_lst[0] + num_lst[1]

ans = ex_bar
if ex_bar-1 >= long_bar:
    ans += long_bar
else:
    ans += ex_bar - 1
    
print(ans)
