# 코드를 작성해주세요
T = int(input())
for t in range(T):
    N = int(input())
    min_cost = [100001, 0]
    for n in range(N):
        W, C = map(int, input().split())
        if min_cost[0] == C/W:
            if min_cost[1] > C:
                min_cost = [C/W, C]
        if min_cost[0] > C/W:
            min_cost = [C/W, C]
    print(min_cost[1])
    