ock = int(input())
if ock == 1:
    print(0)
else:
    A_lst = []
    B_lst = []
    for i in range(ock):
        a, b = map(int, input().split())
        A_lst.append(a)
        B_lst.append(b)
    ans = (max(A_lst) - min(A_lst)) * (max(B_lst) - min(B_lst))
    print(ans)