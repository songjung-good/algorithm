def solution(a, d, included):
    answer = 0
    num = a
    for i in included:
        if i is True :
            answer += num
        num += d
        
    return answer