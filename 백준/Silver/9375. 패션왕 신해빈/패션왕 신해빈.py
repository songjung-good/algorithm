T = int(input())
for t in range(T):
    N = int(input())
    Clothes = {}
    Clothes_cnt = []
    for n in range(N):
        A, B = map(str, input().split())

        if B in Clothes:
            Clothes[B] += 1
        else:
            Clothes[B] = 1

    for cloth in Clothes:
        Clothes_cnt.append(Clothes[cloth])

    ans = 1
    if len(Clothes_cnt) == 1:
        ans = ans + sum(Clothes_cnt)
    else:
        for i in Clothes_cnt:
            ans = ans * (i + 1)

    print(ans - 1)