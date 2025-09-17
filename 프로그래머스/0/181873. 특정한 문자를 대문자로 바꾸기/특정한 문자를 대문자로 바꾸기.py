def solution(my_string, alp):
    answer = ''
    now=ord(alp)
    for i in range(len(my_string)):
        if ord(my_string[i]) == now:
            answer += my_string[i].upper()
        else:
            answer += my_string[i]
    return answer