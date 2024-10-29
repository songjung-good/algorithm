# 단체 수 N, 예산 M, 각 단체의 표 V
N, M = map(int, input().split())
V = list(map(int, input().split()))
# 전체 표의 절반
half_V = sum(V) / 2

V.sort(reverse=True)
CNT = 1
SUM_V = 0
for v in V:
    CNT += 1
    SUM_V += v
    if SUM_V >= half_V:
        break

ans = M // CNT

print(ans)