import math
n1, n2, n12 = map(int, input().split())

ans = (n1 + 1)*(n2 + 1)/(n12 + 1) - 1

print(int(ans))