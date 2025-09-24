def solution(myString, pat):
    num = myString.rfind(pat)
    answer = myString[:num+len(pat)]
    return answer