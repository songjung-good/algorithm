def solution(numLog):
    answer = ''
    num = numLog[0]
    for i in numLog[1:]:
        if i - num == 1:
            answer += 'w'
        elif i - num == -1:
            answer += 's'
        elif i - num == 10:
            answer += 'd'
        else:
            answer += 'a'
        num = i
    return answer