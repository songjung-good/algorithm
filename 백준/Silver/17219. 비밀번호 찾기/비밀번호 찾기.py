import sys

N, M = map(int, sys.stdin.readline().split())
MEMO = {}
for i in range(N):
    SITE, PASSWORD = map(str, sys.stdin.readline().split())
    MEMO[SITE] = PASSWORD

for k in range(M):
    SEARCH = input()
    print(MEMO[SEARCH])