# 코드를 작성해주세요
A = 0
X = 100
for _ in range(4):
    num = int(input())
    A += num
    X = min(X, num)

A -= X

B = 0
X = 100
for _ in range(2):
    num = int(input())
    B+=num
    X = min(X, num)
B -= X

print(A+B)