T = int(input())
for tc in range(1, T+1):
    bingo = [list(map(str, input())) for _ in range(5)]
    ans = ''

    for i in range(15):
        for j in range(5):
            try:
                ans += bingo[j][i]
            except:
                pass

    print(f'#{tc} {ans}')