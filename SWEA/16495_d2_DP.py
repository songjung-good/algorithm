'''

#1
T = int(input())
# 0 -> 0 , 10 -> 1, 20 -> 3
for t in range(1, T+1):
    N = int(input()) // 10
    dp = [0, 1, 3]
    # 0 -> 0 , 10 -> 1, 20 -> 3
    for i in range(3, N + 1):
        dp.append(dp[i-2] * 2 + dp[i - 1])
    result = dp[N]
    print(f'#{t} {result}')
'''
'''
    세로의 길이는 20으로 고정
    가로의 길이는 N(10의 배수)

    붙이는 종이는 20x20과 10x20, 20x10
    만들 수 있는 모든 방법에 필요한 테이프 수

    가로 N/10은 1과 2의 조합으로 만든다.
    가로가 2일때는 1가지 방법이 더 있다. 그러므로 *2 해준다.
'''

'''
    세로의 길이는 20으로 고정
    가로의 길이는 N(10의 배수)

    붙이는 종이는 20x20과 10x20, 20x10
    만들 수 있는 모든 방법에 필요한 테이프 수

    가로 N/10은 1과 2의 조합으로 만든다.
    가로가 2일때는 1가지 방법이 더 있다. 그러므로 *2 해준다.
    2 2 1 / 11 11 1 /  11 2 1 / 2 11 1
    1 2 2
    2 1 2
'''

'''
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())

        cnt_1 = N // 10
        cnt_2 = N // 20
        for i in range(cnt_1):
'''

'''
    10: 1개 10 1개
    20: 3개 10 10 1개 /20 1개
    30: 5개 10 10 10 1개 / 20 10 / 10 20
    40:     10 10 10 10 /10 20 10 / 20 10 10 / 
    50: 21개  13 
    60: 
    70: 85개
'''


# 2
def DP(num):
    lst = [0, 1, 3]

    for i in range(3, num + 1):
        lst.append(lst[i - 2] * 2 + lst[i - 1])

    return lst[num]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    ans = DP(N//10)
    print(f'#{tc} {ans}')
