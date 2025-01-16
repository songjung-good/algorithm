import sys, math
input = sys.stdin.readline

def check(N, num):
    cnt = 2
    start = N
    end = num

    while True:
        now = start - end
        if now < 0:
            break
        else:
            start = end
            end = now
            cnt += 1

    return cnt


N = int(input())
A = math.ceil(N / 8 * 5)
B = math.floor(N / 8 * 4)
max_cnt = 0
max_num = 0

for n in range(B-1, A+1):
    n_cnt = check(N, n)
    if n_cnt > max_cnt:
        max_cnt = n_cnt
        max_num = n

s = N
e = max_num
lst = [N, max_num]
while True:
    now = s - e
    if now < 0:
        break
    else:
        s = e
        e = now
        lst.append(now)

print(max_cnt)
print(*lst)
