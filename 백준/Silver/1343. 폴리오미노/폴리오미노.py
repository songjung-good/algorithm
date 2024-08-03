import sys
input = sys.stdin.readline

WORD = input()
cnt = len(WORD)
ans = ''
check = 0

for i in range(cnt):
    if WORD[i] == 'X':
        check = check + 1
    elif WORD[i] == '.':
        if check:
            four = check // 4
            check = check % 4
            two = check // 2
            check = check % 2
            if check != 0:
                ans = -1
                break
            else:
                if four:
                    ans = ans + ('AAAA' * four)
                if two:
                    ans = ans + ('BB' * two)
        if ans != -1:
            ans = ans + '.'
        else:
            break
    if i == cnt-1:
        four = check // 4
        check = check % 4
        two = check // 2
        check = check % 2
        if check != 0:
            ans = -1
        else:
            if four:
                ans = ans + ('AAAA' * four)
            if two:
                ans = ans + ('BB' * two)
print(ans)
