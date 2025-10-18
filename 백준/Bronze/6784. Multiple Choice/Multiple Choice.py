N= int(input())
lst = [input() for _ in range(N)]
ans = 0
for i in range(N):
    if lst[i] == input():
        ans += 1
print(ans)