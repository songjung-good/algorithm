import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    lst = [[0,0]]
    for n in range(N):
        lst.append([int(input()), n+1])

    cnt = 0
    num = 1
    while cnt <= N:
        num = lst[num][0]
        cnt += 1
        if num == N:
            break
        else:
            pass
    if cnt > N:
        print(0)
    else:
        print(cnt)