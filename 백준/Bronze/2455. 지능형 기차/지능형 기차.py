현재 = 0
최대 = 0
for i in range(4):
    하차, 승차 = map(int, input().split())
    현재 -= 하차
    현재 += 승차
    if 최대 <= 현재:
        최대 = 현재
print(최대)