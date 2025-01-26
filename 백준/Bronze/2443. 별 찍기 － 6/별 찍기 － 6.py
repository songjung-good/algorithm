# 코드를 작성해주세요
N = int(input())
for n in range(N):
    S = '*' * (N - n- 1)
    B = ' ' * n
    print(f'{B}{S}*{S}')
