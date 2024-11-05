# 코드를 작성해주세요
A = int(input())
B = int(input())

C = A % B
D = A % 100
ans = 0

if C > D:
    ans = (B - C) + D
else:
    ans = D - C

while ans >= B:
    ans -= B

if ans == 0:
    print('00')
elif ans < 10:
    print(f'0{ans}')
else:
    print(ans)