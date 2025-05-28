N = int(input())
line = []
for _ in range(N):
    X, Y = map(int, input().split())
    line.append((X, Y))

line.sort()

start = 0
end = 0
cnt = 0
for n in range(N):
    x, y = line[n]
    if start <= x <= end:
        if y > end:
            end = y
    else:
        cnt += end - start
        start = x
        end = y
cnt += end - start
print(cnt)