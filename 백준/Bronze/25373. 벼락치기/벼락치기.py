# 코드를 작성해주세요
N = int(input())
A = N // 7 + 3
if N <= 1:
    print(1)
elif N <= 3:
    print(2)
elif N <= 6:
    print(3)
elif N <= 10:
    print(4)
elif N <= 15:
    print(5)
elif N <= 21:
    print(6)
else:
    if N % 7:
        A += 1
    print(A)