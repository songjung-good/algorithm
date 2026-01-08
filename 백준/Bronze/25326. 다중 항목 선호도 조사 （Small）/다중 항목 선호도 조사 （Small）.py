N, M = map(int, input().split())
favorite_lst = []
for _ in range(N):
    state, fruit, color = input().split()
    favorite_lst.append((state, fruit, color))

for _ in range(M):
    s, f, c = input().split()
    ans = 0
    for st, fr, co in favorite_lst:
        if (s == '-' or s == st) and (f == '-' or f == fr) and (c == '-' or c == co):
            ans += 1
    print(ans)