for tc in range(1, 11):
    ans = 0
    form_len = int(input())
    form = input()

    for i in form:
        if i != '+':
            ans += int(i)

    print(f'#{tc} {ans}')