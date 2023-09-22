N, B = map(str, input().split())
num_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
ans = 0
cnt = 0
for i in N[::-1]:
    line = int(B) ** cnt
    if i not in num_lst:
        ans += (ord(i) - 55) * line
    else:
        ans += int(i) * line
    cnt += 1
print(ans)