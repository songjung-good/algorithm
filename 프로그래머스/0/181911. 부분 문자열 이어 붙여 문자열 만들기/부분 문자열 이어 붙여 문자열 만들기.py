def solution(my_strings, parts):
    answer = ''
    for word, idx in zip(my_strings, parts):
        start, end = idx
        answer += word[start:end+1]
    return answer