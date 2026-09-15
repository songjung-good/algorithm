def solution(triangle):
    cnt = len(triangle)
    for i in range(cnt-1, -1, -1):
        now = triangle[i]
        for j in range(0, i):
            triangle[i-1][j] += max(now[j], now[j+1])

    return triangle[0][0]