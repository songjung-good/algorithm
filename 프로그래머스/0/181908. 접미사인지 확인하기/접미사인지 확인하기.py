def solution(my_string, is_suffix):
    answer = 0
    x = len(is_suffix)
    y = len(my_string)
    if is_suffix == my_string[y-x:y+1]:
        answer = 1
    return answer