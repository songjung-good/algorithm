def solution(n):
    answer = n // 7
    if n % 7:
        answer += 1
    return answer