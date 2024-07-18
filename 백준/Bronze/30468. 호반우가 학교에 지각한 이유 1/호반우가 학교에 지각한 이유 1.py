S, D, I, L ,N = map(int, input().split())

STAT = S + D + I + L
CNT = 0

while True:
    if STAT // 4 >= N:
        print(CNT)
        break
    else:
        STAT += 1
        CNT += 1