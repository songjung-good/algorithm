from collections import deque


def solution(board):
    rows = len(board)
    cols = len(board[0])

    start_r, start_c = -1, -1

    # 시작점 탐색
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "R":
                start_r, start_c = r, c
                break

        # 수정: 0행에서 찾아도 종료되도록 >= 0
        if start_r >= 0:
            break

    queue = deque([(start_r, start_c, 0)])

    # 기존 D[d], D[3-d] 방식도 동작하지만
    # 방향을 명확하게 표현
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    visited = set()

    while queue:
        now_r, now_c, count = queue.popleft()

        if (now_r, now_c) in visited:
            continue

        visited.add((now_r, now_c))

        # 수정: 정지한 위치가 목표점인지 확인
        if board[now_r][now_c] == "G":
            return count

        for dr, dc in directions:
            next_r, next_c = now_r, now_c

            while True:
                check_r = next_r + dr
                check_c = next_c + dc

                # 수정: 범위와 장애물을 함께 검사
                if (
                    check_r < 0
                    or check_r >= rows
                    or check_c < 0
                    or check_c >= cols
                    or board[check_r][check_c] == "D"
                ):
                    break

                next_r = check_r
                next_c = check_c

            # 이동하지 못한 경우
            if (next_r, next_c) == (now_r, now_c):
                continue

            if (next_r, next_c) not in visited:
                queue.append((next_r, next_c, count + 1))

    # 수정: 목표 지점에 도착할 수 없는 경우
    return -1