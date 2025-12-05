def solution(myString):
    answer = ''
    num = ord('l')
    for i in myString:
        if ord(i) < num:
            answer += 'l'
        else:
            answer += i
    return answer