N, M = map(int, input().split())
A, B = max(N-2, 0), max(M-2, 0)

num = (4 * 3) + (A * B * 8) + ((A * 2) + (B * 2)) * 5

print(num // 2)