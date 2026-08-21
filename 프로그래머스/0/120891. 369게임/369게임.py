def solution(order):
    answer = 0
    word=str(order)
    for w in word:
        if w in ['3','6','9']:
            answer += 1
    return answer