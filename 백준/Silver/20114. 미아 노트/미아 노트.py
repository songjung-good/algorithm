N, H, W = map(int, input().split())
MAP = [list(input()) for _ in range(H)]
ans = ''
for n in range(N):
    found = False
    for h in range(H):
        if found:
            break
        for w in range(W):
            now = MAP[h][W*n+w]
            if now != '?':
                ans += now
                found = True
                break
    if not found:
        ans += '?'

print(ans)