# 코드를 작성해주세요
N, M, S = map(int, input().split())

if N < 100 / (M+1):
    print(S*M)
else:
    print(S*(M+1)*(100-N)//100)