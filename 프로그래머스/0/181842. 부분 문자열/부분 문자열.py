def solution(str1, str2):
    answer = 0
    num1, num2 = len(str1), len(str2)
    for i in range(0, num2-num1+1):
        str = str2[i:i+num1]
        if str == str1:
            answer = 1
            break
    return answer