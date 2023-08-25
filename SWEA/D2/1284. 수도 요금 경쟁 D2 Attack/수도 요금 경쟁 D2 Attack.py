'''
A사 : 1리터당 P원의 돈을 내야 한다.

B사 : 기본 요금이 Q원이고,
R리터 이하인 경우 요금은 기본 요금만 청구
R 리터보다 많은 양을 사용한 경우
초과량에 대해 1리터당 S원의 요금을 더 내야 한다.

한 달간 사용하는 수도의 양이 W리터
'''

T = int(input())
for tc in range(1, 1+T):
    P, Q, R, S, W = map(int, input().split())
    #A사 이용시
    A = P * W
    # B사 이용시
    if W > R:
        B = Q + (W - R) * S
    else:
        B = Q
    ans = [A, B]

    print(f'#{tc} {min(ans)}')