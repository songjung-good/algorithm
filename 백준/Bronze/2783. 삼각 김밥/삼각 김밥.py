X, Y = map(int, input().split())
N = int(input())
MIN_COST = 1000 / Y * X
for n in range(N):
    X1, Y1 = map(int, input().split())
    cost = 1000 / Y1 * X1
    if MIN_COST > cost:
        MIN_COST = cost

MIN_COST = round(MIN_COST, 2)
print(MIN_COST)