
for tc in range(1, 11):
    #변의 길이(고정 100)
    size = int(input())
    #자석이 놓인 테이블 1=N극 2=S극
    table = [list(map(int, input().split())) for _ in range(size)]
    #n과 s가 맞 닿는 횟수
    ans = 0
    #같은 열 기준으로 비교한다.
    for j in range(size):
        for i in range(size):
            #N극 이면서 마지막 행이 아니면
            if table[i][j] == 1 and i < size -1:
                for k in range(1, size - i):
                    if table[i+k][j] == 1:
                        break
                    elif table[i+k][j] == 2:
                        ans += 1
                        break

    print(f'#{tc} {ans}')
