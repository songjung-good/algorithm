def find_num(s, e, num):
    mid = (s + e) // 2
    if s >= e:
        return B_lst[mid]
    else:
        L = abs(B_lst[mid] - num)
        R = abs(B_lst[mid+1] - num)
        if L <= R:
            return find_num(s, mid, num)
        else:
            return find_num(mid+1, e, num)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = sorted(list(map(int, input().split())))
    # C_lst = []
    ans = 0
    for i in A_lst:
        # C_lst.append(find_num(0, m-1, i))
        ans += find_num(0, m-1, i)
    print(ans)