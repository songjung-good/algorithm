DAY, TOTAL = map(int, input().split())
CHANGE = list(map(int, input().split()))
CNT = 0
DAY = 0
for i in CHANGE:
    CNT += i
    if CNT < 0:
        CNT = 0
    elif CNT >= TOTAL:
        DAY += 1

print(DAY)