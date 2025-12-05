def solution(arr):
    answer = []
    i = 0
    
    while i < len(arr):
        if answer:
            if arr[i] == answer[-1]:
                answer.pop()
            else:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
        i += 1
    
    if not answer:
        answer.append(-1)
    return answer