N, M = map(int, input().split())
IMG = [input() for _ in range(N)]
new_IMG = ['' for _ in range(N)]

for n in range(N):
    for m in range(M):
        new_IMG[n] = new_IMG[n] + IMG[n][m] * 2

check_IMG = [input() for _ in range(N)]

if new_IMG == check_IMG:
    print('Eyfa')
else:
    print('Not Eyfa')