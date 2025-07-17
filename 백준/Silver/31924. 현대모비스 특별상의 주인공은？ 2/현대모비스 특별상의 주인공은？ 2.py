import sys
input = sys.stdin.readline

N = int(input())
MAP = [list(input()) for _ in range(N)]
Dx = [1, 1, 0, -1, -1, -1, 0, 1]
Dy = [0, 1, 1, 1, 0, -1, -1, -1]
word = ['M', 'O', 'B', 'I', 'S']
ans = 0
for r in range(N):
    for c in range(N):
        if MAP[r][c] == 'M':
            for d in range(8):
                cnt = 1
                if 0 <= r + (4 * Dx[d]) < N and 0 <= c + (4 * Dy[d]) < N:
                    if MAP[r+Dx[d]][c+Dy[d]] == 'O':
                        cnt += 1
                        for i in range(2, 5):
                            if MAP[r + (Dx[d] * i)][c + (Dy[d] * i)] == word[i]:
                                cnt += 1
                if cnt == 5:
                    ans += 1

print(ans)