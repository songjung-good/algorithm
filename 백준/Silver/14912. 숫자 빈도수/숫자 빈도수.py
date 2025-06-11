n, d = map(int, input().split())
lst = [i for i in range(1, n+1)]
cnt = 0
for i in lst:
    for j in str(i):
        if j == str(d):
            cnt += 1

print(cnt)