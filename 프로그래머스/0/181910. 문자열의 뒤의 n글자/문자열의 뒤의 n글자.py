def solution(my_string, n):
    answer = ''
    N = len(my_string) - n
    answer += my_string[N:]
    
    return answer