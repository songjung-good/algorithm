import math

N = int(input())

pairings = math.factorial(N) // (2**(N//2) * math.factorial(N//2))

print(pairings)