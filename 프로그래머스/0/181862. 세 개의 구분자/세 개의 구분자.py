def solution(myStr):
    num = len(myStr)
    start = -1
    answer = []
    for n in range(num):
        if myStr[n] in ['a', 'b', 'c']:
            if start != -1:
                answer.append(myStr[start:n])
                start = -1
        else:
            if start == -1:
                start = n
    if start != -1:
        answer.append(myStr[start:num+1])
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer