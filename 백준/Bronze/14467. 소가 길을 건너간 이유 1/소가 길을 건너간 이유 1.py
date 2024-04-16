N = int(input())
cow = [0,2,2,2,2,2,2,2,2,2,2]
ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    if cow[A] == 2:
        cow[A] = B
    elif cow[A] != B:
        cow[A] = B
        ans += 1
    else:
        pass

print(ans)