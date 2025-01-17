# 코드를 작성해주세요
N = int(input())
lst = list(map(int, input().split()))

Y = 0
M = 0
for n in range(N):
    now = lst[n]
    Y += now // 30 + 1
    M += now // 60 + 1

Y = Y * 10
M = M * 15

if Y == M:
    print(f'Y M {Y}')
elif Y < M:
    print(f'Y {Y}')
else:
    print(f'M {M}')