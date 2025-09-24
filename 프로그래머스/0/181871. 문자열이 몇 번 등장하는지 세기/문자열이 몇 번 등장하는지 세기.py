def solution(myString, pat):
    answer = 0
    index = 0
    while index > -1:
        index = myString.find(pat, index)
        if index == -1:
            break
        else:
            answer += 1
            index += 1
    return answer