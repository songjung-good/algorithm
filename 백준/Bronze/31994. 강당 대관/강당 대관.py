word = ''
max_cnt = 0
for _ in range(7):
    N, K = map(str, input().split())
    k = int(K)
    if max_cnt < k:
        max_cnt = k
        word = N

print(word)