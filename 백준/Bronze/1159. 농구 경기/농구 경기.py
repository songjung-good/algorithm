# import sys
# input = sys.stdin.readline

team = []
N = int(input())
for i in range(N):
    member = input()
    team.append(member[0])

answer = ''
cnt = 0
now = ''
team.sort()
for j in team:
    if j != now:
        if cnt >= 5:
            answer += now
        cnt = 1
        now = j
    else:
        cnt += 1

if cnt >= 5:
    answer += now

if answer:
    print(answer)
else:
    print('PREDAJA')
# team = [map(input().split()) for _ in range(N)]
# print(N)
# print(team)

