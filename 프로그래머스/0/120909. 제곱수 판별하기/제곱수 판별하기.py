def solution(n):
    answer = 0
    num = n ** 0.5
    if num == int(num):
        answer = 1
    else:
        answer = 2
    return answer