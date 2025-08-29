import sys
input = sys.stdin.readline

def find_coor(now, next):
    nowl, nowr = now
    nextl, nextr = next
    return abs(nowl - nextl) + abs(nowr - nextr) + 1

# 키보드
KEYBOARD = [list(map(str, 'qwertyuiop')),
            list(map(str, 'asdfghjkl0')),
            list(map(str, 'zxcvbnm000'))
            ]

# 입력
now_L, now_R = map(str, input().split())
word = input()

# 위치 값 저장
L_word = ''
L_coor = (-1, -1)
R_word = ''
R_coor = (-1, -1)

# 초기 위치 세팅
for r in range(3):
    for c in range(10):
        if KEYBOARD[r][c] == now_L:
            L_coor = (r, c)
        if KEYBOARD[r][c] == now_R:
            R_coor = (r, c)

# 오른손으로 치는 글자
right = 'yuiophjklbnm'
ans = 0
# 손가락 옮기기
for w in word:
    for r in range(3):
        num = 5
        if r == 2:
            num = 4
        # 오른손
        if w in right:
            for c in range(num, 10):
                if KEYBOARD[r][c] == w:
                    ans += find_coor(R_coor, (r, c))
                    R_coor = (r,c)
                    R_word = w
        # 왼손
        else:
            for c in range(num):
                if KEYBOARD[r][c] == w:
                    ans += find_coor(L_coor, (r, c))
                    L_coor = (r,c)
                    L_word = w

print(ans)