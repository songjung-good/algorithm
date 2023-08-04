'''
    D = 두 기차 사이의 거리
    A = A기차 속력
    B = B기차 속력
    F = 파리의 속력

    A와 B가 맞닿는 시간 까지 반복
    
    B지점과 F가 만나는 거리
'''

#1
T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    # A_d = (A * time)
    # B_d = D - (B * time)
    ans = 0

    while D > 0:
        time1 = D / (F + B)
        D -= time1 * (A + B)
        ans += 1

        time2 = D / (F + A)
        D -= time2 * (A + B)
        ans += 1

    print(f'#{tc} {ans}')



#2
T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    # A_d = (A * time)
    # B_d = D - (B * time)
    ans = 0




    print(f'#{tc} {ans}')