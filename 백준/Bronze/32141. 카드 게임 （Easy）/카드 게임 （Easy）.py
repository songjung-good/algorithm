# 코드를 작성해주세요
N, H = map(int, input().split())
N_lst = sorted(list(map(int, input().split())))

if H > sum(N_lst):
    print(-1)
    
else:
    num = 0
    for n in range(N):
        num += N_lst[n]
        if H <= num:
            break
    print(n+1)