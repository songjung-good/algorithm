# 코드를 작성해주세요
K = int(input())
for k in range(K):
    n, s, d = map(int, input().split())
    D=s*d
    cnt = 0
    for _ in range(n):
        di, vi = map(int, input().split())
        if D >= di:
            cnt += vi

    print(f'Data Set {k+1}:')
    print(cnt)
    print()
