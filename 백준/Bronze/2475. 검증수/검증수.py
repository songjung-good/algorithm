# 입력값 받기
A = input().strip().split()
check = 0
for i in range(5):
    check += int(A[i]) ** 2

ans = check % 10
print(ans)