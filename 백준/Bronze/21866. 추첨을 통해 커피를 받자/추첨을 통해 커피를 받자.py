# 코드를 작성해주세요
q_score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
a_score = list(map(int, input().split()))

cnt = 0
ans = 'none'
for i in range(9):
    if a_score[i] > q_score[i]:
        ans = 'hacker'
        break
    else:
        cnt += a_score[i]

if cnt >= 100:
    ans = 'draw'

print(ans)