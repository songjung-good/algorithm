def change(bit):
    cnt = 0
    check = -1
    ans = ''
    for i in bit:
        if i == '1':
            cnt = cnt + 1
            ans = ans + '1'
        elif i == '0':
            ans = ans + '0'
        elif i == 'e':
            if cnt % 2 == 0:
                ans = ans + '0'
            else:
                ans = ans + '1'
        elif i == 'o':
            if cnt % 2 == 0:
                ans = ans + '1'
            else:
                ans = ans + '0'
    return ans

while True:
    bit = input()
    if bit == '#':
        break
    else:
        ans = change(bit)
        print(ans)
