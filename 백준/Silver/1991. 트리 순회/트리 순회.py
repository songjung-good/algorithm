from collections import deque
import sys
input = sys.stdin.readline


graph = [[0,0] for _ in range(27)]

N = int(input())
for _ in range(N):
    n, l, r = input().split()
    n = ord(n) - 64
    if l != '.':
        graph[n][0] = ord(l) - 64
    if r != '.':
        graph[n][1] = ord(r) - 64

def preorder(now):
    if now == 0:
        return
    print(chr(now + 64), end='')
    preorder(graph[now][0])
    preorder(graph[now][1])

def inorder(now):
    if now == 0:
        return
    inorder(graph[now][0])
    print(chr(now + 64), end='')
    inorder(graph[now][1])

def postorder(now):
    if now == 0:
        return
    postorder(graph[now][0])
    postorder(graph[now][1])
    print(chr(now + 64), end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)