T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())            #N은 행과 열, M은 찾아야하는 글자의 길이
    arr = [list(input()) for _ in range(N)]

    word = ''
    for i in range(N):
        for j in range(N-M+1):
            k = 0
            while k < M:
                if arr[i][j+k] != arr[i][j+M-k-1]:
                    break
                k += 1
            if k == M:
                word = ''.join(arr[i][j+k] for k in range(M))

    for j in range(N):
        for i in range(N-M+1):
            k = 0
            while k < M:
                if arr[i+k][j] != arr[i+M-k-1][j]:
                    break
                k += 1
            if k == M:
                word = ''.join(arr[i+k][j] for k in range(M))

    print(f'#{tc} {word}')
