def selecSort(lst, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    ans_lst = ' '.join(map(str, lst))

    return ans_lst

T = int(input())
for tc in range(1, T+1):
    N_input = int(input())
    lst_input = list(map(int, input().split()))
    ans = selecSort(lst_input, N_input)
    print(f'#{tc} {ans}')