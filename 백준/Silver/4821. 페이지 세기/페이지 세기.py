while True:
    page = int(input())
    ans = [0] * 1001
    if page == 0:
        break
    else:
        print_lst = list(map(str, input().split(',')))
        # print(print_lst)
        for p in print_lst:
            lst = list(map(int, p.split('-')))
            if len(lst) == 1:
                low = int(lst[0])
                if page >= low:
                    ans[low] = 1
            else:
                low, high = lst[0], lst[1]
                if low > high or low > page:
                    pass
                else:
                    for i in range(low, min(high, page)+1):
                        ans[i] = 1
    print(sum(ans))