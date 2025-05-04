import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
res = False
while N >= cnt:
    N -= cnt
    cnt += 1
    if res:
        res = False
    else:
        res = True

if res:
    print(0)
else:
    print(cnt - N)
