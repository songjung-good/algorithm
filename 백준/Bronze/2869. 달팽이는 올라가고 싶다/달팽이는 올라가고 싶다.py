import math

A, B, V = map(int, input().split())
step = A - B
goal = V - A

ans = math.ceil(goal/step)

print(ans+1)
