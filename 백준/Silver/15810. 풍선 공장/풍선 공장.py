import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time_lst = list(map(int, input().split()))

# 이분 탐색 초기값 설정
min_time = 1  # 최소 1분은 필요
max_time = min(time_lst) * M  # 최대로 걸릴 수 있는 시간

# 이분 탐색 시작
while min_time < max_time:
    time = (min_time + max_time) // 2  # 중간 시간 계산
    cnt = 0

    # 현재 시간 내에 만들 수 있는 풍선 개수 계산
    for t in time_lst:
        cnt += time // t

    # 풍선 개수가 M 이상이면 시간을 줄인다
    if cnt >= M:
        max_time = time
    else:
        min_time = time + 1

print(min_time)  # 최소 시간을 출력