X = int(input())
cnt = 0
while X != 1:
    if X % 2 == 1:
        X += 1
    else:
        X = X // 2
    cnt += 1

print(cnt)