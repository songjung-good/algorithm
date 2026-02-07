N,M = map(int, input().split())
min_P, min_S = float('inf'), float('inf')
for _ in range(M):
    P, S = map(int, input().split())
    min_P, min_S = min(min_P, P), min(min_S, S)

print(min((N//6 * min_P + N%6 * min_S), min_S*N, (N//6 + 1) *min_P))