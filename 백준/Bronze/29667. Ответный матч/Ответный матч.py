# 코드를 작성해주세요
A1, B1 = map(int, input().split(':'))
B2, A2 = map(int, input().split(':'))

ans = 'NO'
if A1 == B2 and B1 == A2:
    ans = 'YES'
if B1 >= A2 and A1 >= B2:
    ans = 'YES'

print(ans)