# 코드를 작성해주세요
N = int(input())
A, B = map(int, input().split())
ans = 4
if A == 1 or A == N:
    ans -= 1
if B == 1 or B == N:
    ans -= 1
if N == 1:
    ans -= 2

print(ans)
    