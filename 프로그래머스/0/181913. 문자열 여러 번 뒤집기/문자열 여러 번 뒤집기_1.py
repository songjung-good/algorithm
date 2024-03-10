# 틀린 코드 
#  왜 틀린 건지 모르겠다...
def solution(my_string, queries):
    # answer = ''
    for s, e in queries:
        word = my_string[s:e+1]
        new_word = word[::-1]
        # new_word = word.reversed()
        my_string = my_string.replace(word, new_word)
    answer = my_string
    return answer