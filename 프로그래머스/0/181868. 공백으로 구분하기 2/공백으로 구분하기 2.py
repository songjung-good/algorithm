def solution(my_string):
    answer = []
    word = ''
    for i in my_string:
        if i == ' ':
            if word != '':
                answer.append(word)
                word = ''
        else:
            word += i
    if word != '':
        answer.append(word)
    return answer