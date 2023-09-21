A, B = map(str, input().split())

A = A[::-1]
B = B[::-1]
ans = max(int(A), int(B))
print(ans)