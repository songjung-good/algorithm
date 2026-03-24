# 코드를 작성해주세요
A = int(input())
B = int(input())
C = A + B

ans = 1
while True:
    if C // (10**ans) >= 1:
        ans += 1
    else:
        break
print(ans)