def solution(array):
    lst = [0] * (max(array) + 1)
    
    for a in array:
        lst[a] += 1
    
    num = max(lst)
    cnt = 0
    for a in lst:
        if num == a:
            cnt += 1
    if cnt > 1:
        answer = -1
    else:
        answer = lst.index(num)
    return answer