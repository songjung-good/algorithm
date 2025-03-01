import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
X = int(input())

# 시작과 끝이 다른 블럭일 때
start = BOARD[0][0]
end = BOARD[N-1][M-1]
if start != end:
    print('DEAD')
    exit()

# 이동 가능한 좌표
D = [(i, j) for i in range(X+1) for j in range(X+1) if i+j <= X and (i, j) != (0, 0)]
D += [(-i, j) for i, j in D]
D += [(i, -j) for i, j in D]
# 스택 기반 DFS
stack = [(0, 0)]  # 시작점
visit = set()
visit.add((0, 0))

# dfs
while stack:
    x, y = stack.pop()

    if (x, y) == (N-1, M-1):
        print("ALIVE")
        exit()

    # 이동 가능한 방향 탐색
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and BOARD[nx][ny] == start and (nx, ny) not in visit:
            visit.add((nx, ny))
            stack.append((nx, ny))

print("DEAD")