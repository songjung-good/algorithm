# 코드를 작성해주세요
N = int(input())
MAP = [list(map(str, input())) for _ in range(N)]
D = [1, -1, 0, 0]
V = [[0]*N for _ in range(N)]
ans = []

for r in range(N):
    for c in range(N):
        # 집 여부 확인
        if MAP[r][c] == '0':
            pass
        else:
            # 방문 여부 확인
            if V[r][c] == 1:
                pass
            else:
                Q = [(r,c)]
                V[r][c] = 1
                cnt = 1
                while Q:
                    x, y = Q.pop()
                    for d in range(4):
                        nx = x + D[d]
                        ny = y + D[3-d]
                        if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] == '1' and V[nx][ny] == 0:
                            Q.append((nx, ny))
                            V[nx][ny] = 1
                            cnt += 1
                ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i)