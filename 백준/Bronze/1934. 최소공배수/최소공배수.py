N = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
for _ in range(N):
    A, B = map(int, input().split())
    lcm = (A * B) // gcd(A, B)
    print(lcm)
