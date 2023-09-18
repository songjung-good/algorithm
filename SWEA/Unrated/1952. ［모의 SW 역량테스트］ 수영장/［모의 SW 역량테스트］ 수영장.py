T = int(input())
for t in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))

    min_cost = year

    cost = [0] * 12
    for i in range(12):
        cost[i] = min(plan[i] * day, month) + cost[i-1]
        cost[i] = min(cost[i], cost[i-3] + three_month)

    if min_cost > cost[-1]:
        min_cost = cost[-1]

    print(f'#{t} {min_cost}')