a, b = map(int, input().split())
if a % 2 == 0 or b % 2 == 0:
    print(0)
else:
    A, B = max(a, b), min(a, b)
    print(((A//2 + 1) * B) - (A//2 * B))
    