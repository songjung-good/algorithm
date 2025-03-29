def solution(my_string, m, c):
    answer = ''
    num = len(my_string)
    for n in range(num):
        if n % m + 1 == c:
            answer += my_string[n]
    return answer