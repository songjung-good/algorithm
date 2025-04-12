def solution(n, k):
    answer = []
    i = 1
    now = k
    while now <= n:
        answer.append(now)
        i += 1
        now = k * i
    return answer