
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # print(f'#{t} {N} {K} {A}')

    cnt = 0     #합이 K가 되는 경우의 수
    for i in range(1<<N):       #부분집합을 표시하는 i
        s = 0       #부분집합의 합
        for j in range(N): #j번 비트
            if i & (1<<j):  #i의 j번 비트 검사
                s += A[j]
        if s == K:
            cnt += 1

    print(f'#{t} {cnt}')