def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    now = 0
    for i in range(1, n**2 + 1):
        if 0 <= x < n and 0 <= y < n and answer[x][y] == 0:
            answer[x][y] += i
        else:
            x, y = x - dx[now], y - dy[now]
            now = (now + 1) % 4
            x, y = x + dx[now], y + dy[now]
            answer[x][y] += i
        x, y = x + dx[now], y + dy[now]
    return answer