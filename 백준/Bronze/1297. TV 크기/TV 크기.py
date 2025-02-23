import math
D, H, W = (map(int,input().split()))

d = math.sqrt(H ** 2 + W ** 2)
a = D / d

print(int(H * a), int(W*a))