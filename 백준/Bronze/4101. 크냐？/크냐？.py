while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:  # 두 정수가 모두 0이면 반복문을 종료합니다.
        break
    if A > B:
        print('Yes')
    else:
        print('No')