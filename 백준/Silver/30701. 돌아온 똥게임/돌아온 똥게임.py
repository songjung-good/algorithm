import heapq
N, D = map(int, input().split())
monsters = []
items = []
ans = 0
for _ in range(N):
    A, X = map(int, input().split())
    if A == 1:
        heapq.heappush(monsters, X)
    else:
        heapq.heappush(items, X)
        ans += 1

while monsters:
    while items and monsters[0] >= D:
        D *= heapq.heappop(items)

    if monsters[0] < D:
        D += heapq.heappop(monsters)
        ans += 1
    else:
        break

print(ans)