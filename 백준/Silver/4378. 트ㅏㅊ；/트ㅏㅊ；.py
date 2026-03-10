# 코드를 작성해주세요
KEYBOARD = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        ans = ''
        for w in input():
            if w == ' ':
                ans += ' '
            else:
                m = -1
                for l in KEYBOARD:
                    if l == w:
                        ans += KEYBOARD[m]
                        break
                    else:
                        m += 1
        print(ans)
    except:
        exit()

