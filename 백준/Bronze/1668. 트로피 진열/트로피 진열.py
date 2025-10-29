N = int(input())
lst = [int(input()) for _ in range(N)]

past = 0
cnt = 0
for i in range(N):
    if lst[i] > past:
        cnt += 1
        past = lst[i]
print(cnt)

past = 0
cnt = 0
for i in range(N-1, -1, -1):
    if lst[i] > past:
        cnt += 1
        past = lst[i]
print(cnt)
