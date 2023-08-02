T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())        #N은 가로,세로길이, M은 단어의 길이
    blank = []

    for _ in range(N):
        blank.append(list(map(int, input().split())))

    word = 0            # 빈칸 수
    ans = 0             # 정답 수

    for i in range(N):              #가로
        for j in range(N):
            if blank[i][j] == 0:    #빈칸이 없으면
                if K == word:       # 빈칸과 단어의 길이가 같으면 정답
                    ans += 1
                word = 0            # 빈칸 0으로 초기화
            elif blank[i][j] == 1:  #빈칸이 있으면
                word += 1           #빈칸 추가
                if j == N-1:        #끝에 도달하면
                    if word == K:   #빈칸과 단어길이 조사
                        ans += 1
                    word = 0

    for j in range(N):              #세로
        for i in range(N):
            if blank[i][j] == 0:
                if K == word:
                    ans += 1
                word = 0
            elif blank[i][j] == 1:
                word += 1
                if i == N-1:
                    if word == K:
                        ans += 1
                    word = 0

    print(f'#{tc} {ans}')
