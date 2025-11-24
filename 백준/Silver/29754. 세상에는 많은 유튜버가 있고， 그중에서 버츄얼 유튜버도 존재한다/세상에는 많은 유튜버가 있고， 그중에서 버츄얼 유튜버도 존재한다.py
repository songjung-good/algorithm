import sys
from datetime import timedelta
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

weeks = M // 7

for _ in range(N):
    name, day, s_t, e_t = input().split()
    s_h, s_m = map(int, s_t.split(':'))
    e_h, e_m = map(int, e_t.split(':'))
    diff = timedelta(hours=e_h, minutes=e_m) - timedelta(hours=s_h, minutes=s_m)
    sec = diff.total_seconds()

    w = (int(day) - 1) // 7

    if name in dic:
        dic[name][w][0] += 1
        dic[name][w][1] += sec
    else:
        dic[name] = [[0, 0] for _ in range(weeks)]
        dic[name][w] = [1, diff.total_seconds()]

b_time = 60**3
ans_check = False
for key in sorted(dic.keys()):
    check = True
    for j in range(weeks):
        if dic[key][j][0] < 5 or dic[key][j][1] < b_time:
            check = False
            break

    if check:
        if ans_check:
            print(key)
        else:
            ans_check = True
            print(key)

if not ans_check:
    print(-1)