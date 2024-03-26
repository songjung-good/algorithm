A = input()
cnt = 0
ans = ''
for i in A:
    if cnt == 0:
        ans += i
        cnt = 1
    elif i == '-':
        cnt = 0
print(ans)