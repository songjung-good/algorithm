# 코드를 작성해주세요
N, M = map(int, input().split())
lst = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    lst[A-1] += 1
    lst[B-1] += 1

for i in lst:
    print(i)