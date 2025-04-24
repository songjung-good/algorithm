a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 * n0 + a0 <= c * n0:
    if a1 <= c:
        print(1)
        exit(0)
print(0)