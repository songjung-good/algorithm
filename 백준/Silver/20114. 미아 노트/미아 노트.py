N, H, W = map(int, input().split())
MAP = [list(input()) for _ in range(H)]
ans = ''
for n in range(N):
    word = ''
    for h in range(H):
        for w in range(W):
            now = MAP[h][W*n+w]
            if now == '?':
                pass
            else:
                word = now
                break
        if word != '':
            break
    if word == '':
        ans += '?'
    else:
        ans += word

print(ans)