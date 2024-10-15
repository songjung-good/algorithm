# 코드를 작성해주세요
N = int(input())
N_lst = list(map(int, input().split()))

seat = []
cnt = 0
for n in range(N):
    A = N_lst[n]
    if A in seat:
       cnt += 1
    else:
        seat.append(A)

print(cnt)