A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    cnt = C - B
    print(A // cnt + 1)