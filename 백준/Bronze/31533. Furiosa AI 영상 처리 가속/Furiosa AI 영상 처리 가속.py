# 코드를 작성해주세요
a = int(input())
m,n = map(int, input().split())

A = min(m,n)
B = max(m,n)

X = (A / a) * 2
Y = max(B / a, A)

print(min(X, Y))