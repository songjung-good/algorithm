N = int(input())
S_flower = list(map(int, input().split()))
Q = int(input())
for q in range(Q):
    Query = list(map(int, input().split()))
    # 꽃 개수 출력
    if Query[0] == 1:
        l = Query[1]-1
        r = Query[2]
        k = Query[3]
        new_list = S_flower[l:r]
        cnt = 0
        for a in new_list:
            if a == k:
                cnt = cnt + 1
        print(cnt)
    # 꽃 밟기
    else:
        l = Query[1]-1
        r = Query[2]
        for i in range(l, r):
            S_flower[i] = 0
