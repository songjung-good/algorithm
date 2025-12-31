# 코드를 작성해주세요
N = int(input())
for _ in range(N):
    A, B = map(int,input().split())
    if A < B:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')