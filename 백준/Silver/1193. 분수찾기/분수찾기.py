goal = int(input())
cnt = 1
past_num = 0
last_num = 0
while True:
    if goal > last_num:
        past_num = last_num
        last_num += cnt
        cnt += 1
    else:
        break

#홀수면
if cnt % 2:
    left = 1
    for i in range(past_num+1, last_num+1):
        right = cnt - left
        if i == goal:
            break
        else:
            left += 1

else:
    right = 1
    for i in range(past_num+1, last_num+1):
        left = cnt - right
        if i == goal:
            break
        else:
            right += 1

print(f'{left}/{right}')