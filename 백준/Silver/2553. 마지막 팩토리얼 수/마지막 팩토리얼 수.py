import math
N = int(input())
num = math.factorial(N)

S = str(num)[::-1]
for s in S:
    if s != '0':
        print(s)
        break
