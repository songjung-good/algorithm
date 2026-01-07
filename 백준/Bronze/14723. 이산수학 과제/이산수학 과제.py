N = int(input())
NUM = 0
cnt = 1
while True:
    NUM += cnt
    if N <= NUM:
        break
    else:
        cnt += 1

now = cnt - (NUM - N)
print(cnt - now + 1, now)