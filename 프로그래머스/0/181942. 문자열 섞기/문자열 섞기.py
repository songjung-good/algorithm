def solution(str1, str2):
    num = len(str1)
    answer = ""
    for i in range(num):
        answer = answer + str1[i]
        answer = answer + str2[i]
    return answer