def solution(polynomial):
    answer = ''
    A, B = 0, 0
    now, end = 0, len(polynomial)

    while now < end:
        if polynomial[now].isdigit():

            # 수정: 연속된 숫자를 모두 읽기
            num = 0
            while now < end and polynomial[now].isdigit():
                num = num * 10 + int(polynomial[now])
                now += 1

            # 수정: 숫자 다음이 x인지 확인
            if now < end and polynomial[now] == 'x':
                A += num
                now += 1
            else:
                B += num

        else:
            if polynomial[now] == 'x':
                A += 1

            now += 1

    if A == 0:
        answer = str(B)

    elif B == 0:
        # 수정: 1x → x
        answer = 'x' if A == 1 else str(A) + 'x'

    else:
        # 수정: 1x + B → x + B
        answer = ('x' if A == 1 else str(A) + 'x') + ' + ' + str(B)

    return answer