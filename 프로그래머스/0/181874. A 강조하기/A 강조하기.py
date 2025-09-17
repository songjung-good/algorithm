def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] == 'a' or myString[i] == 'A':
            answer += 'A'
        else:
            answer += myString[i].lower()
    return answer