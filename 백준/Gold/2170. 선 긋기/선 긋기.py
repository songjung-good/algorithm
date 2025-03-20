import sys
input = sys.stdin.readline

N = int(input())
line = []
for _ in range(N):
    start, end = map(int, input().split())
    line.append((start, end))
line.sort()
start, end = line.pop(0)
ans = abs(end - start)
for l in line:
    s, e = l
    if s > end:
        start = s
        end = e
        ans += abs(end - start)
    else:
        if e <= end:
            pass
        else:
            ans += abs(e - end)
            end = e

print(ans)