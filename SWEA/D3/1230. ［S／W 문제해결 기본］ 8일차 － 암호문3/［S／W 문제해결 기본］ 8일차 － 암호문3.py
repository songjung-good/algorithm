'''
 I(삽입) x, y, s
 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.
 [ ex) I 3 2 123152 487651 ]
 D(삭제) x, y
 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제한다.[ ex) D 4 4 ]
 A(추가) y, s
 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다. s는 덧붙일 암호문들이다. [ ex) A 2 421257 796813 ]
'''

for tc in range(1, 11):
    #원본암호 길이
    N = int(input())
    #원본암호
    origin_psw = list(map(int, input().split()))
    #변경 횟수
    make_psw = int(input())
    #변경 내용
    new_psw = list(map(str, input().split()))

    while new_psw:
        now = new_psw.pop(0)
        if now == 'I':
            point = int(new_psw.pop(0))
            num_cnt = int(new_psw.pop(0))
            for _ in range(num_cnt):
                s = int(new_psw.pop(0))
                origin_psw.insert(point, s)
                point += 1
        elif now == 'D':
            point = int(new_psw.pop(0))
            for _ in range(int(new_psw.pop(0))):
                origin_psw.pop(point)
        elif now == 'A':
            for _ in range(int(new_psw.pop(0))):
                origin_psw.append(int(new_psw.pop(0)))

    ans = []
    for i in range(10):
        ans.append(origin_psw[i])

    print(f'#{tc}', end=' ')
    print(*ans)