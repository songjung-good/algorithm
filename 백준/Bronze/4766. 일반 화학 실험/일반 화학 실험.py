past = 999
while True:
    temp = float(input())
    if temp == 999:
        break
    else:
        if past == 999:
            pass
        else:
            ans = float(temp - past)
            print(f'{ans:.2f}')
        past = temp