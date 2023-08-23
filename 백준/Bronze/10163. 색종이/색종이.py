#색종이의 장 수
N = int(input())
#색종이가 놓이는 평면
field = [[0] * 1001 for _ in range(1001)]
#답
cnt_lst = [0] * N

# 좌하단의 좌표 X, Y, 너비, 높이가 순서대로 입력
for k in range(N):
    ldx, ldy, wide, height = map(int, input().split())
    cnt = 0
    for i in range(ldy, ldy+height):
        for j in range(ldx, ldx+wide):
            if field[i][j] != 0:
                #기존의 필드에 적힌 값
                A = field[i][j]
                #해당 값을 기록한 인덱스에서 1만큼 줄인다.
                cnt_lst[A-1] -= 1
                #
            field[i][j] = k+1
            cnt += 1

    cnt_lst[k] = cnt

for i in range(N):
    if cnt_lst[i] < 0:
        print(0)
    else:
        print(cnt_lst[i])