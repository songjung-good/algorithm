def solution(str_list):
    answer = []
    for n in range(len(str_list)):
        word=str_list[n]
        if word == 'l' or word == 'r':
            if word == 'l':
                answer = str_list[:n]
            else:
                answer = str_list[n+1:]
            break
    return answer