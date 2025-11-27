a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))
c_lst = list(map(int,input().split()))
d_lst = list(map(int,input().split()))
b_lst.sort(reverse=True)
c_lst.sort(reverse=True)
d_lst.sort(reverse=True)

cnt = min(a_lst)
pre_ans = sum(b_lst) + sum(c_lst) + sum(d_lst)
print(pre_ans)

ans = 0
for _ in range(cnt):
    ans += b_lst.pop(0) // 10 * 9
    ans += c_lst.pop(0) // 10 * 9
    ans += d_lst.pop(0) // 10 * 9
ans += sum(b_lst) + sum(c_lst) + sum(d_lst)

print(ans)