N = int(input())
TIME = 0
for n in range(N):
    # a초 휴식, b초 탐색, start 탐색시작시간, end종료시간
    a, b = map(int, input().split())
    A = TIME // (a+b)
    start = A * (a+b)
    end = start + b
    if TIME >= start and TIME <= end:
        TIME = end+1
    else:
        TIME = TIME+1

print(TIME)