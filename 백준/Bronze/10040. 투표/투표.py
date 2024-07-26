N, M = map(int, input().split())
cost = []
votes = [0] * N
for i in range(N):
    cost.append(int(input()))

for j in range(M):
    A = int(input())
    for k in range(N):
        if cost[k] <= A:
            votes[k] += 1
            break
        else:
            pass

max_votes = max(votes)
max_index = votes.index(max_votes) + 1  # 0부터 시작하므로 1을 더해 경기 번호로 변경
print(max_index)