while True:
    num = input()
    if num == '0':
        break
    else:
        ans = [num]
        while True:
            num = ans[-1]
            check = len(num)
            if check == 1:
                print(*ans)
                break
            else:
                number = 1
                for i in num:
                    number *= int(i)
                ans.append(str(number))