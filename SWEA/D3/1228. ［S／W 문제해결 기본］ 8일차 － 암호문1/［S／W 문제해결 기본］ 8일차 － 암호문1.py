'''
 I(삽입) x, y, s
 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.
 [ ex) I 3 2 123152 487651 ]
 1228. [S/W 문제해결 기본] 8일차 - 암호문1
'''
for tc in range(1, 11):
    N = int(input())
    #원본암호
    origin_psw = list(map(int, input().split()))
    #변경 횟수
    make_psw = int(input())
    #변경 내용
    new_psw = list(map(str, input().split()))

    #x는 위치 y는 숫자 개수
    x = 0
    y = 0
    past_num = 101
    for i in new_psw:
        if i == 'I':
            pass
        elif int(i) < 100:
            if past_num >= 100:
                x = int(i)
            else:
                y = int(i)
            past_num = int(i)
        else:
            origin_psw.insert(x, int(i))
            x += 1
            past_num = int(i)

    ans = []
    for i in range(10):
        ans.append(origin_psw[i])

    print(f'#{tc}', end=' ')
    print(*ans)