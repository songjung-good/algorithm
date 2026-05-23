def solution(my_str, n):
    answer = []
    num=len(my_str)
    s=0
    while s < num:
        answer.append(my_str[s:s+n])
        s+=n
    return answer