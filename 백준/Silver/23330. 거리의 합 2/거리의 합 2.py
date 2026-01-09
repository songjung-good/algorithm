import sys
input = sys.stdin.readline

n = int(input().strip())
x = list(map(int, input().split()))

x.sort()

prefix = 0
pair_sum = 0

for i, v in enumerate(x):
    pair_sum += v * i - prefix
    prefix += v

print(pair_sum * 2)