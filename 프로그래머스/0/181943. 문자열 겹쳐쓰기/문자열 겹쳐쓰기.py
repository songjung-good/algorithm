def solution(my_string, overwrite_string, s):
    a=len(my_string)
    b=len(overwrite_string)
    word1 = my_string[:s]
    word2 = my_string[b+s:]
    # if a > b+s:
    
    answer = word1 + overwrite_string + word2    
    
    return answer