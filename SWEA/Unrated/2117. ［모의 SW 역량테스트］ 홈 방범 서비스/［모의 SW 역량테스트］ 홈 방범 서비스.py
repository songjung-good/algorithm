'''
N*N 크기의 도시
운영 비용 = K * K + (K - 1) * (K - 1)

서비스 범위 만큼 마을 탐색

1. 전체를 다 덮으려면 사이즈 어떻게 할까요?
 1) 전체 집 수, 전체 비용 먼저 탐색
2. 하나씩 줄이면서 탐색
 1)
 abs(row - center_row) + abs(col - center_col) <= radius:
'''

#시작 좌표를 기준으로 주변의 집의 수 탐색
def diamond_search(center_row, center_col, radius):
    house = 0
    min_row = center_row - radius
    min_col = center_col - radius
    if min_col < 0:
        min_col = 0
    if min_row < 0:
        min_row = 0
    for row in range(min_row, center_row + radius):
        for col in range(min_col, center_col + radius):
            if 0 <= row < N and 0 <= col < N and abs(row - center_row) + abs(col - center_col) < radius:
                if town[row][col] == 1:
                    house += 1
    return house



T = int(input())
for tc in range(1, T+1):
    #N 마을의 크기, M 가구 당 지불 가능 비용
    N, M = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]
    #정답
    ans = 0
    #H 총 가구 수
    H = 0
    for i in range(N):
        H += sum(town[i])
    #총 비용, 최대범위
    max_price = N * N + (N - 1) * (N - 1)
    #최대 범위가 커버되면 통과
    if H*M > max_price:
        ans = H
    #아니면 처음부터 탐색 ㅠㅠ
    else:
        #행
        for i in range(N):
            #열
            for j in range(N):
                #범위
                for k in range(N, 0, -1):
                    #비용, 집의 수, 받는 돈
                    price = k * k + (k - 1) * (k - 1)
                    house_cnt = diamond_search(i, j, k)
                    income = house_cnt * M
                    #넓은 범위 부터 탐색이라 통과되면 바로 종료
                    if price <= income:
                        if ans < house_cnt:
                            ans = house_cnt
                            break

    print(f'#{tc} {ans}')