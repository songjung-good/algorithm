N = input()
now = len(N)
ans = ''

if now == 1:
    print(N)

else:
    check = 0
    for i in range(1, now):
        num = int(N[-i])
        if check == 1:
            num += 1
        if num >= 5:
            check = 1
        else:
            check = 0
        ans += '0'
    
    num = int(N[0]) + check
    print(str(num) + ans)
        