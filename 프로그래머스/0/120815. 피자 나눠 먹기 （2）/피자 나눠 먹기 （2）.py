def solution(n):
    answer = 1
    while True:
        if (6 * answer) % n == 0:
            break
        else:
            answer += 1
    return answer