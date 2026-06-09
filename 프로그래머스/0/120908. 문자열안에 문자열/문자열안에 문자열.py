def solution(str1, str2):
    answer = 2
    A, B = len(str1), len(str2)
    for i in range(0, A-B+1):
        print(str1[i:i+B])
        if str1[i:i+B] == str2:
            answer = 1
            break
    return answer