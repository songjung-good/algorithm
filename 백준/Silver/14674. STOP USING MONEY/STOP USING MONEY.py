N, K = map(int, input().split())
games = []
for _ in range(N):
    i, c, h = map(int, input().split())
    games.append((i, c, h, h * 1e9 // c))  # h/c 대신 정수 기반의 가성비 계산

# 정렬: 가성비 내림차순 -> 가격 오름차순 -> 번호 오름차순
sorted_games = sorted(
    games,
    key=lambda x: (-x[3], x[1], x[0])
)

# 상위 K개 게임 번호 출력
for i in range(K):
    print(sorted_games[i][0])
