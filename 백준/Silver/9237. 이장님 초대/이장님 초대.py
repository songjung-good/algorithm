import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
for i in range(N):
    trees[i] = trees[i] + i + 2

print(max(trees))