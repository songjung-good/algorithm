def solution(my_string, target):
    answer = 0
    num1, num2 = len(my_string), len(target)
    for i in range(num1-num2+1):
        str = my_string[i:num2+i]
        if str == target:
            answer = 1
            break
        
    return answer