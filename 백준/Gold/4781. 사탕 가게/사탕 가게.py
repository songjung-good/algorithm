import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n = int(n)
    if n == 0 and m == 0.00:
        break
    else:
        candy = []
        for _ in range(n):
           c, p = map(float, input().split())
           candy.append([int(c), int(p * 100 + 0.5)])  # 가격을 정수로 변환

        m = int(m * 100 + 0.5)  # 예산을 정수로 변환

        # DP 테이블 초기화
        DP = [0] * (m + 1)

        # DP 테이블 갱신
        for cal, price in candy:
            for j in range(price, m + 1):
                DP[j] = max(DP[j], DP[j - price] + cal)

        # 최대 칼로리 출력
        print(DP[m])