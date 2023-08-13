'''
    NxM 의 풍선 판
    중앙을 기준으로 상하좌우
    첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M,
    이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.
'''

def max_flower(row, col, lst):
    row_d = [0, 1, 0, -1]
    col_d = [1, 0, -1, 0]
    max_num = 0

    for i in range(row):
        for j in range(col):
            sum_num = lst[i][j]
            for k in range(4):
                ni = i + row_d[k]
                nj = j + col_d[k]
                if 0 <= ni < row and 0 <= nj < col:
                    sum_num += lst[ni][nj]
            if max_num < sum_num:
                max_num = sum_num

    return max_num

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_balloon = [list(map(int, input().split())) for _ in range(N)]

    ans = max_flower(N, M, lst_balloon)
    print(f'#{tc} {ans}')