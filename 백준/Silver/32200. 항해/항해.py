# 코드를 작성해주세요
N, X, Y = map(int, input().split())
sandwich = list(map(int, input().split()))
gap = Y - X

A = 0
B = 0
for n in range(N):
    cnt = sandwich[n] // X
    left = sandwich[n] % X
    if left > (gap * cnt):
        num = left - (gap * cnt)
    else:
        num = 0
    A += cnt
    B += num
        
print(A)
print(B)