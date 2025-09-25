def solution(myString, pat):
    answer = 0
    word = ''
    for i in myString:
        if i == 'A':
            word += 'B'
        else:
            word += 'A'
    if pat in word:
        answer = 1
    return answer