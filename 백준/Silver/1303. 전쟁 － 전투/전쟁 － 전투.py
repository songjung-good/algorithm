from collections import deque
import sys

input = sys.stdin.readline

def main():
    # 입력값 받기
    M, N = map(int, input().split())  # M: 가로, N: 세로
    soldiers = [input().strip() for _ in range(N)]  # 병사 배치 정보

    # 각 팀의 힘
    w_power = 0
    b_power = 0

    # 방문 위치 확인
    visited = [[False] * M for _ in range(N)]

    # 상하좌우 이동을 위한 좌표
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                # BFS 시작
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                team = soldiers[i][j]
                cnt = 1

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if not visited[nx][ny] and soldiers[nx][ny] == team:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                cnt += 1

                # 팀에 따라 힘 계산
                if team == 'W':
                    w_power += cnt ** 2
                else:
                    b_power += cnt ** 2

    # 결과 출력
    print(w_power, b_power)

if __name__ == "__main__":
    main()