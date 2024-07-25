import sys

N = int(input())
for n in range(N):
    WORD = ''
    while True:
        a = sys.stdin.readline().rstrip()
        if a == '':
            break
        WORD += a

    cnt = len(WORD)
    check = WORD.count('#')

    if check == 0:
        print('Efficiency ratio is 100%.')
    else:
        ans = round(100 - (check / cnt * 100), 1)
        if ans.is_integer():
            ans = int(ans)
        else:
            pass
        print(f'Efficiency ratio is {ans}%.')