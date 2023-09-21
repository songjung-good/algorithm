score_board = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0,
}

score = 0
class_cnt = 0

for i in range(20):
    A, B, C = map(str, input().split())
    if C != 'P':
        score += float(B) * score_board.get(C)
        class_cnt += float(B)
ans = score/class_cnt
print(round(ans, 6))
