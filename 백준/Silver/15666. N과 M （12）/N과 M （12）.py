# 코드를 작성해주세요
def combi(n, cnt, lst):
    for i in range(cnt, num):
        lst[n] = N_lst[i]
        if n == M-1:
            print(*lst)
        else:
            combi(n+1, i, lst)
    return 


N, M = map(int, input().split())
N_lst = sorted(list(set(map(int,input().split()))))
num = len(N_lst)
ans = [0] * M
combi(0, 0, ans)