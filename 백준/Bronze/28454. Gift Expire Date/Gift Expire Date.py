import sys
input = sys.stdin.readline

now_day = input()
N = int(input())
cnt = 0
for n in range(N):
    gift = input()
    if now_day <= gift:
        cnt = cnt + 1

print(cnt)