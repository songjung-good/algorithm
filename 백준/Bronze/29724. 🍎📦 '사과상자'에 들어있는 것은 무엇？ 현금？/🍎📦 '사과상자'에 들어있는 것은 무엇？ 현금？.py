N = int(input())
weight = 0
won = 0
for _ in range(N):
    T, W, H, L = map(str, input().split())
    if T == 'A':
        apple = (int(W) // 12) * (int(H) // 12) * (int(L) // 12)
        weight += apple * 500 + 1000
        won += 4000 * apple
    else:
        weight += 6000

print(weight)
print(won)