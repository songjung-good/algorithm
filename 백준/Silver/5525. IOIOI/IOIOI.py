import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()

cnt = 0
answer = 0
i = 1

while i < M - 1:
    if S[i-1:i+2] == "IOI":
        cnt += 1
        if cnt >= N:
            answer += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(answer)
