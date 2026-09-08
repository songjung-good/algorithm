def solution(n):
    answer = 1
    if n in [0, 1, 2]:
        pass
    else:
        num = (n+1)//2 + 1
        num_lst = [i for i in range(0, (n+1)//2+1)]
        for i in range(1, num):
            num_lst[i] = num_lst[i] + num_lst[i-1]

        # print(num_lst)
        s, e = 0, 1
        while s < e:
            now = num_lst[e] - num_lst[s]
            if now == n:
                answer += 1
                e += 1
            elif now > n:
                s += 1
            else:
                e += 1
            if e >= num or s >= num:
                break

    return answer