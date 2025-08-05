import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
word = input()

start = 0
end = M - (N * 2)
ans = 0
while start < end:
    if word[start] == 'I':
        now=start + 1
        if word[now:now+N*2] == 'OI' * N:
            ans += 1
    start += 1

print(ans)
