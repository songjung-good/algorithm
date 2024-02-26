def solution(n):
    answer = 0
    if n == 1:
        answer = 1
    elif n % 2 == 1:
        answer += n
        for i in range(n//2):
            answer += 2*i + 1
    else:
        for i in range(n//2):
            a = 2 * (i+1)
            answer += a ** 2
    return answer