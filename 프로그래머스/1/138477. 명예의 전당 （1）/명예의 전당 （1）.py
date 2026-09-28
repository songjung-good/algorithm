def solution(k, score):
    answer = []
    result = []
    for s in score:
        answer.append(s)
        answer.sort(reverse=True)
        if len(answer) > k:
            result.append(answer[k-1])
        else:
            result.append(answer[-1])
    return result