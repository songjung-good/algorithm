N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)

ans = 0
for i in range(N):
    ans += max(lst[i] - i, 0)

print(ans)