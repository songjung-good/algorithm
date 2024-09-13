Y2, M2, D2 = map(int, input().split())
Y1, M1, D1 = map(int, input().split())

if D1 < D2:
    M1 = M1 - 1
    D1 = D1 + 30
if M1 < M2:
    Y1 = Y1 - 1
    M1 = M1 + 12

DAYS = (Y1 - Y2) * 360 + (M1 - M2) * 30 + (D1 - D2)
YEARS = DAYS // 360
YEAR = 0
if YEARS == 0:
    pass
else:
    for y in range(YEARS):
        YEAR += y // 2 + 15

MONTHS = DAYS // 30
if MONTHS > 36:
    MONTHS = 36

print(YEAR, MONTHS)
print(f'{DAYS}days')
