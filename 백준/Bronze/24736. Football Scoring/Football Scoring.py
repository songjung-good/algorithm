ans = []
for _ in range(2):
    T, F, S, P, C = map(int, input().split())
    score = T * 6 + F * 3 + S * 2 + P * 1 + C * 2
    ans.append(score)
print(*ans)