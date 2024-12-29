import sys
input = sys.stdin.readline

def count(NUM):
    number = 0
    for num in range(1, NUM+1):
        number += num
    return number

N = int(input())
I = str(input())

ans = 0
cnt = 0
for n in range(N):
    if I[n] == '0':
        ans += count(cnt)
        cnt = 0
    else:
        cnt += 1

ans += count(cnt)
print(ans)
