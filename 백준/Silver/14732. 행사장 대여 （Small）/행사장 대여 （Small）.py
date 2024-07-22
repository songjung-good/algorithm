N = int(input())
MAP = [[0] * 501 for _ in range(501)]
cnt = 0
for n in range(N):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if MAP[i][j] != 1:
                cnt += 1
                MAP[i][j] = 1
            else:
                pass

print(cnt)
