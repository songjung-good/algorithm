N, K = map(int, input().split())
countries = []

for _ in range(N):
    idx, g, s, b = map(int, input().split())
    countries.append((idx, g, s, b))

# 금 > 은 > 동 기준 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
ranks = dict()
ranks[countries[0][0]] = rank

for i in range(1, N):
    # 이전 국가와 메달 수가 모두 같으면 같은 순위
    if countries[i][1:] == countries[i-1][1:]:
        ranks[countries[i][0]] = rank
    else:
        rank = i + 1
        ranks[countries[i][0]] = rank

print(ranks[K])
