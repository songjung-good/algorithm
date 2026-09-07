def solution(X, Y):
    answer = []
    X_lst, Y_lst = [0] * 10, [0] * 10
    for x in X:
        X_lst[int(x)] += 1
    for y in Y:
        Y_lst[int(y)] += 1
    
    check = False
    for i in range(9, -1, -1):
        if X_lst[i]:
            if Y_lst[i]:
                if i != 0:
                    check = True
                if X_lst[i] == Y_lst[i]:
                    answer.append(str(i) * X_lst[i])
                else:
                    answer.append(str(i) * min(X_lst[i], Y_lst[i]))
                

    if len(answer) == 0:
        return '-1'
    else:
        if check:
            ans = '' 
            for a in answer:
                ans += a
            return ans
        else:
            return '0'
        
    return answer