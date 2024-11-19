A, B, C, D, E = map(int, input().split())
CNT = 0

# 5kg물건
CNT += E

# 4kg물건
CNT += D
A = max(0, A - D)

# 3kg물건
CNT += C
if B >= C:
    B -= C
else:
    TRI_ONE = 2 * (C - B)
    A = max(0, A - TRI_ONE)
    B = 0

# 2kg물건
if B % 2 == 1:
    TWO = B // 2 + 1
    CNT += TWO
    A -= TWO + 2
else:
    TWO = B // 2
    CNT += TWO
    A -= TWO

# 1kg 물건
if A > 0:
    CNT += (A + 4) // 5

print(CNT)

