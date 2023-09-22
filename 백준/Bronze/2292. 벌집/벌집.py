goal = int(input())

a_goal = goal - 1
cnt = 1
if goal != 1:
    while True:
        if a_goal <= cnt*6:
            cnt += 1
            break
        else:
            a_goal = a_goal - cnt*6
            cnt += 1

print(cnt)