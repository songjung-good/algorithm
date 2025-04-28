import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))

cnt = 0
e = 0
for i in range(N):
    now_s = lst[i][0]
    now_e = lst[i][1]
    if e > now_s:
        pass
    else:
        e = now_e
        cnt += 1

print(cnt)