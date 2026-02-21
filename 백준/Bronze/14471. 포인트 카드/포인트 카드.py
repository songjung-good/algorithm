# 코드를 작성해주세요
N, M = map(int, input().split())
lst = []
cnt = 0
for _ in range(M):
    A, B = map(int, input().split())
    if A >= N:
        cnt += 1
    else:
        lst.append(B - N)

if cnt < M-1:
    lst.sort()
    print(sum(lst[:M-cnt-1]))
else:
    print(0)