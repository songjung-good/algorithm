def solution(my_string, s, e):
    answer = ''
    answer = my_string[:s]+ ''.join(reversed(my_string[s:e+1])) + my_string[e+1:]
    return answer