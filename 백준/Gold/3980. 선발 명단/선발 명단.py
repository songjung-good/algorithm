def find_best(N, lst):
    global P
    if N == 11:
        global max_num
        if max_num < sum(lst):
            max_num = sum(lst)
            return
    else:
        now_p=P[N]
        for i in range(11):
            if now_p[i] != 0 and lst[i] == 0:
                lst[i]=now_p[i]
                find_best(N+1, lst)
                lst[i]=0
            elif i == 10:
                return 

T=int(input())
for _ in range(T):
    P = [list(map(int, input().split())) for _ in range(11)]
    max_num = 0
    find_best(0, [0]*11)
    print(max_num)