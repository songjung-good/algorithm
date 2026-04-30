def solution(money):
    answer = []
    a=money//5500
    c=money-(a*5500)
    answer.append(a)
    answer.append(c)
    return answer