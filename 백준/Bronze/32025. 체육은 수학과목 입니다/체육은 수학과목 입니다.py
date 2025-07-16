import sys
input = sys.stdin.readline

H = int(input())
W = int(input())

num = min(H, W)
ans = int(num / 2 * 100)

print(ans)
