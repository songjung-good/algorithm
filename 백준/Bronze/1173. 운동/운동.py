# 운동 시간 N, 최소 맥박 m, 최대 맥박 M, 운동후 증가 T, 휴식후 감소 R
N, m, M, T, R = map(int, input().split())

now_m = m
total_time = 0
ex_time = 0

if M - m < T:
    print(-1)
    exit()

while ex_time < N:
    if now_m + T <= M:
        now_m += T
        ex_time += 1
        total_time += 1
    else:
        now_m -= R
        total_time += 1

    if now_m > M:
        print(-1)
        exit()
    elif now_m < m:
        now_m = m
    else:
        pass

print(total_time)