# 코드를 작성해주세요
A, B =map(int, input().split())
C = int(input())

CASH =A + B
C2 = C *2
if CASH >= C2:
    print(CASH - C2)
else:
    print(CASH)