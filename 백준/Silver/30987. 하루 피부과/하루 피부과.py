# 코드를 작성해주세요
x1, x2 = map(int, input().split())
a, b1, c1, b2, c2 = map(int, input().split())
b = b1 - b2
c = c1 - c2

ans = (a//3 * (x2**3) + b//2 * (x2**2) + c * x2 ) - (a//3 * (x1**3) + b//2 * (x1**2) + c * x1)
print(ans)
