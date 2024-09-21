N, M = map(int, input().split())
first_lap = [0]
last_lap = [0]
for n in range(N):
    score = int(input())
    first_lap.insert(score, n+1)

first_lap = first_lap[0:M+1]

for m in range(M):
    score = int(input())
    last_lap.insert(score, first_lap[-(m+1)])

for i in range(3):
    print(last_lap[i+1])