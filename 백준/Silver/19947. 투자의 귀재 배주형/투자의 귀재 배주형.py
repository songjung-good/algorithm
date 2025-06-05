A, B, C = 1.05, 1.2, 1.35
H, Y = map(int, input().split())
DP = [H] * (Y+1)

for y in range(1, Y+1):
    if y < 3:
        DP[y] = int(DP[y-1] * A)
    elif 3 <= y < 5:
        a = int(DP[y-1] * A)
        b = int(DP[y-3] * B)
        DP[y] = max(a, b)
    elif y >= 5:
        a = int(DP[y-1] * A)
        b = int(DP[y-3] * B)
        c = int(DP[y-5] * C)
        DP[y] = max(a, b, c)

print(DP[Y])