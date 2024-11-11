N = int(input())
income = list(map(int, input().split()))
cost = list(map(int, input().split()))

max_income = max(income)  # 전체 최대 이익값 계산
result = []

for i in range(N):
    mx_ic = max_income if income[i] != max_income else max(income[:i] + income[i+1:])
    chance = mx_ic - cost[i]
    net = income[i] - cost[i] - chance
    result.append(net)

print(" ".join(map(str, result)))
