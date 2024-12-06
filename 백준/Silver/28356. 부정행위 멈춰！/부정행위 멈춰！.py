import sys

input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [[0] * M for _ in range(N)]
used = [False] * 5

ans = [0] * 5  # 숫자별 사용 횟수

for n in range(N):
    prev_row = 0
    for m in range(M):
        for i in range(5):
            used[i] = False

        if n > 0:
            used[MAP[n - 1][m]] = True
        if m > 0:
            used[prev_row] = True
        if n > 0 and m > 0:
            used[MAP[n - 1][m - 1]] = True
        if n > 0 and m < M - 1:
            used[MAP[n - 1][m + 1]] = True

        for num in range(1, 5):
            if not used[num]:
                MAP[n][m] = num
                ans[num] += 1
                break

        prev_row = MAP[n][m]

# 최소 사용되지 않은 숫자 계산
for x in range(1, 5):
    if ans[x] == 0:
        print(x - 1)
        break
else:
    print(4)
for row in MAP:
    print(*row)
