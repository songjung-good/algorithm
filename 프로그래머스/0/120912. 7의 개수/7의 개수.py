def solution(array):
    answer = 0
    for a in array:
        for s in str(a):
            if s == '7':
                answer+=1
    return answer