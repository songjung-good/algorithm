# 코드를 작성해주세요
N, M, L = map(int, input().split())
lst = [0] * N

now = 0
cnt = 0
while True:
    if lst[now] % 2:
        now = (now + L) % N
        lst[now] += 1
    else:
        now = now - L
        if now < 0:
            now += N
        lst[now] += 1

    if lst[now] >= M:
        break
    cnt += 1


print(cnt)