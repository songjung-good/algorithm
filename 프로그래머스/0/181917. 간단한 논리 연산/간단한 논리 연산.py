def solution(x1, x2, x3, x4):
    answer = True
    if x1 is False and x2 is False:
        answer = False
    else:
        if x3 is False and x4 is False:
            answer = False
    return answer