def solution(slice, n):
    answer = 1
    while True:
        if slice * answer >= n:
            break
        else:
            answer += 1
    return answer