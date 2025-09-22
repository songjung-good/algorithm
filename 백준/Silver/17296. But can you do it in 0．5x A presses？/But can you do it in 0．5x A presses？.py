import sys
input = sys.stdin.readline

N = int(input())
stage = list(map(float, input().split()))
cnt = 0
check = 0

for n in range(N):
    click = stage[n]

    if check:
        if click:
            cnt += int(click)

    else:
        if click:
            if cnt == 0 and int(click) != click:
                cnt += 1
            cnt += int(click)
            check = 1

print(cnt)