# 코드를 작성해주세요
K = int(input())
for k in range(K):
    P, M = map(int, input().split())
    SEAT = []
    cnt = 0
    for p in range(P):
        A = int(input())
        if A in SEAT:
            cnt += 1
        else:
            SEAT.append(A)
        
    print(cnt)