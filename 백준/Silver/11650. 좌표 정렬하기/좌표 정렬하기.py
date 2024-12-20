import sys
input = sys.stdin.readline

DICT = []
N = int(input())
for n in range(N):
    a, b = map(int, input().split())
    DICT.append([a,b])

DICT = sorted(DICT)

for d in DICT:
    print(*d)