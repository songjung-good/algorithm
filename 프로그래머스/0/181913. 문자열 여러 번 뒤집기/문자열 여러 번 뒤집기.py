def solution(my_string, queries):
    for s, e in queries:
        word = my_string[s:e + 1]
        new_word = word[::-1]
        my_string = my_string[:s] + new_word + my_string[e + 1:]
    answer = my_string
    return answer