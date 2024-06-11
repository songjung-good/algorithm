T = int(input())
CHECK = 'AABBABB'

for _ in range(T):
    ans = 1
    word = input()
    cnt = 0
    # 1, 2 조건 체크
    if len(word) != 7:
        ans = 0
    else:
        KEY1 = word[0]
        KEY2 = word[2]
        if KEY1 == KEY2:
            ans = 0
        else:
            for i in word:
                if CHECK[cnt] == 'A':
                    if i == KEY1:
                        pass
                    else:
                        ans = 0
                else:
                    if i == KEY2:
                        pass
                    else:
                        ans = 0
                cnt += 1
    print(ans)