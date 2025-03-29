def solution(my_string):
    answer = []
    num = len(my_string)
    for i in range(num):
        char = my_string[i:num+1]
        if char in answer:
            pass
        else:
            answer.append(char)
    answer.sort()
    return answer