T = int(input())



for tc in range(1, T+1):
    N, M = map(int, input().split())            #N은 행과 열, M은 찾아야하는 글자의 길이
    arr = [list(map(str, input().split())) for _ in range(N)]

    word = ''
    for i in range(N):
        for j in range(N-M+1):
            for k in range(M):
                if arr[i][j+k] == arr[i][j+M-k]:
                    word += arr[i][j+k]
                elif arr[i][j+k] != arr[i][j+M-k]:
                    word = ''

    print(f'#{tc} {word}')
