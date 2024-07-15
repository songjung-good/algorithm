# N은 문항 수 , M은 응시자 수, SCORE는 문항의 배점
N, M = map(int, input().split())
SCORE = list(map(int, input().split()))

# DICT형태로 답안 받기
RESULT = {}
for i in range(M):
    line = input().strip().split()
    key = int(line.pop(0))
    RESULT[key] = line

# 최고점과 해당 점수 받은 번호
MAX_SCORE = -1
MAX_NUM = -1

# 응시자 수 반복
for i, key in enumerate(RESULT):
    NOW = 0
    # 문항 수 반복
    for j in range(N):
        if RESULT[key][j] == 'O':
            NOW += SCORE[j]
        else:
            pass
    if MAX_SCORE < NOW:
        MAX_SCORE = NOW
        MAX_NUM = key
    elif MAX_SCORE == NOW and MAX_NUM > key:
        MAX_NUM = key
    else:
        pass

print(MAX_NUM, MAX_SCORE)