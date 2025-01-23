import sys
input = sys.stdin.readline

D = [(0,0), (0,1), (1,0), (1,1)]

N, M, K = map(int, input().split())
TILES = [input().strip('\n') for _ in range(N)]
CNT = 0
TILE = [''] * K
for x in range(K):
    for y in range(K):
        check = {}
        for n in range(N//K):
            for m in range(M//K):
                tile = TILES[x + (n * K)][y + (m * K)]
                if tile in check:
                    check[tile] += 1
                else:
                    check[tile] = 1
        max_char = max(check, key=check.get)
        TILE[x] += max_char
        CNT += check[max_char]


CNT = N*M - CNT
print(CNT)
TILE *= N//K
for t in TILE:
    print(t * (M//K))
